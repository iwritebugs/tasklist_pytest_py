import tasks
import pytest


@pytest.mark.smoke
def test_smoke():
    t1 = tasks.Task()
    assert t1 is not None


def test_defaults():
    task = tasks.Task()
    assert task == (None, None, False, None)


def test_member_access():
    task = tasks.Task('Summary', 'Owner', False, 1)
    assert task.summary == 'Summary'
    assert task.owner == 'Owner'
    assert task.done == False
    assert task.id == 1


@pytest.mark.skipif(tasks.__version__ >= '0.1.0',
                    reason='Skipped after version 0.1.0')
def test_version():
    assert False
