import logging

import pytest
import os
from pathlib import Path

from sn_agent import ontology
from sn_agent.ontology.settings import OntologySettings
from sn_agent.test.mocks import MockApp
from sn_agent.log import setup_logging

log = logging.getLogger(__name__)

TEST_DIR = Path(__file__).parent

@pytest.fixture
def app():
    app = MockApp()
    ontology.setup_ontology(app)
    return app

def test_ontology(app):
    # Test that there is an ontology assigned to the app.
    app_ontology = app['ontology']
    assert not app_ontology is None

    # Test the standard services for the demo services.
    service_name = app_ontology.get_service_name(ontology.DOCUMENT_SUMMARIZER_ID)
    assert(service_name == 'Document Summarizer')
    service_name = app_ontology.get_service_name(ontology.WORD_SENSE_DISAMBIGUATER_ID)
    assert(service_name == 'Word Sense Disamnbiguater')
    service_name = app_ontology.get_service_name(ontology.FACE_RECOGNIZER_ID)
    assert(service_name == 'Face Recognizer')
    service_name = app_ontology.get_service_name(ontology.TEXT_SUMMARIZER_ID)
    assert(service_name == 'Text Summarizer')
    service_name = app_ontology.get_service_name(ontology.VIDEO_SUMMARIZER_ID)
    assert(service_name == 'Video Summarizer')
    service_name = app_ontology.get_service_name(ontology.ENTITY_EXTRACTER_ID)
    assert(service_name == 'Entity Extracter')


def test_bogus_yaml_config(app):
    app = MockApp()
    setup_logging()
    settings = OntologySettings()
    original_config_file = settings.CONFIG_FILE
    log.debug("ontology original config file {0}".format(original_config_file))

    # Test missing service ontology_node_id
    log.debug("ontology os.environ config file {0}".format(original_config_file))
    yaml_file = os.path.join(TEST_DIR, "ontology_test.yml")
    os.environ['SN_ONTOLOGY_CONFIG_FILE'] = yaml_file
    exception_caught = False
    try:
        ontology.setup_ontology(app)
    except RuntimeError as exception:
        exception_caught = True
        log.debug("    Expected Exception caught %s", exception)
    except:
        pass
    assert(exception_caught)

    # Test missing service ontology_node_id
    log.debug("ontology os.environ config file {0}".format(original_config_file))
    yaml_file = os.path.join(TEST_DIR, "ontology_test_2.yml")
    os.environ['SN_ONTOLOGY_CONFIG_FILE'] = yaml_file
    exception_caught = False
    try:
        ontology.setup_ontology(app)
    except RuntimeError as exception:
        exception_caught = True
        log.debug("    Expected Exception caught %s", exception)
    except:
        pass
    assert(exception_caught)

    # Test missing service ontology_node_id
    log.debug("ontology os.environ config file {0}".format(original_config_file))
    yaml_file = os.path.join(TEST_DIR, "ontology_test_3.yml")
    os.environ['SN_ONTOLOGY_CONFIG_FILE'] = yaml_file
    exception_caught = False
    try:
        ontology.setup_ontology(app)
    except RuntimeError as exception:
        exception_caught = True
        log.debug("    Expected Exception caught %s", exception)
    except:
        pass
    assert(exception_caught)


    os.environ['SN_ONTOLOGY_CONFIG_FILE'] = original_config_file
