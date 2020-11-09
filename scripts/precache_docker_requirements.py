#!/usb/bin/env python3
import pathlib
import logging
import argparse
from collections import defaultdict

import yaml
import docker

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

###TODO
"""
Configure docker client connection startup for local dev

"""


def configure_logger(args):
    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    if args.debug:
        ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)


def get_docker_uri(cwl):
    try:
        with open(cwl) as fh:
            data = yaml.load(fh, Loader=yaml.FullLoader)
            requirements = data.get('requirements', {})
            for req in requirements:
                if req['class'] == 'DockerRequirement':
                    return req['dockerPull']
    except yaml.scanner.ScannerError as e:
        logger.debug(f'Scanning Error {cwl}: {e}')
    return None


def precache_docker_images(docker_requirements):
    client = docker.from_env()
    for r in docker_requirements.keys():
        try:
            logger.info(f'Getting image: {r}')
            image = client.images.get(r)
        except docker.errors.ImageNotFound as e:
            logger.debug(f'{e}')
            logger.info(f'Pulling {r}, this may take a moment...')
            image = client.images.pull(r)
        except docker.errors.APIError as e:
            print(e)
        finally:
            logger.info(f'Found: {image.short_id} {image.tags}')


if __name__ == '__main__':
    app_desc = """Precache docker images by..."""
    parser = argparse.ArgumentParser(description=app_desc)
    parser.add_argument('-d', '--debug', action='store_true', help='')
    parser.add_argument('-t', '--tools-location', default='modules', help='')
    args = parser.parse_args()

    # Configure logger
    configure_logger(args)

    # Fetch docker tags from CWL docs
    docker_tags = defaultdict(int)
    for cwl in pathlib.Path(args.tools_location).glob('*.cwl'):
        logger.info(cwl)
        r = get_docker_uri(cwl)
        if r:
            docker_tags[r] += 1

    # Perform precaching
    precache_docker_images(docker_tags)
