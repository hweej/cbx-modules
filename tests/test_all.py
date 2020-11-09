import pytest
import os

FIXTURE_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
)

@pytest.fixture
def cwltools(pytestconfig):
    class Basedir:
        modules=os.path.join(pytestconfig.rootdir, 'modules')
        tests=os.path.join(pytestconfig.rootdir, 'tests')
        data=os.path.join(pytestconfig.rootdir, 'tests', 'data')

    return Basedir


@pytest.mark.validate
class TestValidateCWLTools:
    """ Requires cwltool """
    @pytest.mark.parametrize("tool,tool_input,expected", [
        ("cutadapt-2.5_single.cwl", 'cutadapt-2.5_single_inputs.yml', 'Something expected'),
        # ("ex1.cwl", 'cutadapt-2.5_single_inputs.yml', 'Something expected'),
        ("hello_world.cwl", 'hello_world_inputs.yml', 'Something expected'),
        ("cutadapt-2.5_single.cwl", 'cutadapt_single_inputs.yml', 'Something expected'),])
    def test_run_cwltool_validate(self, tool, tool_input, expected, virtualenv, cwltools):
        try:
            runtime_exe = virtualenv.run(['cwltool', '--validate', os.path.join(cwltools.modules, tool)], capture=True)
        except Exception as e:
            pytest.fail(e)
        finally:
            assert 'is valid CWL' in runtime_exe


# @pytest.mark.skip(reason='Skipping optional I/O docker integration')
@pytest.mark.integration
class TestDockerIntegration:
    @pytest.mark.parametrize("tool,tool_input,expected", [
        ("cutadapt-2.5_single.cwl", 'cutadapt-2.5_single_inputs.yml', 'Something expected'),
        ("hello_world.cwl", 'hello_world_inputs.yml', 'Something expected'),
        # ("ex1.cwl", 'cutadapt-2.5_single_inputs.yml', 'Something expected'),
        ])
    def test_run(self, tool, tool_input, expected, virtualenv, cwltools):
        try:
            runtime_exe = virtualenv.run([
            'cwltool', '--debug', os.path.join(cwltools.modules, tool), os.path.join(cwltools.tests, tool_input)], capture=True)
            print(runtime_exe)
        except Exception as e:
            pytest.fail(e)
        finally:
            assert 'Final process status is success' in runtime_exe

