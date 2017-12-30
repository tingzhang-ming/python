from datetime import datetime
import abc


class Task(object):
    """
    An abstract class representing a task that must run, 
    and which should track individual runs and results.
    """
    def __init__(self):
        self.runs = []

    def run(self):
        start = datetime.now()
        result = self._run()
        end = datetime.now()
        self.runs.append({
            'start': start,
            'end': end,
            'result': result,
        })
        return result

    def _run(self):
        raise NotImplementedError('Task subclass must define a _run method.')

# ---------------------------------------------------------------------------------------


class TaskMeta(type):
    """
    A metaclass that ensures the presence of a _run method 
    on any non-abstract classes it creates.
    """

    def __new__(cls, name, bases, attrs):
        # If this is an abstract class, do not check for a _run method.
        if attrs.pop('abstract', False):
            return super(TaskMeta, cls).__new__(cls, name, bases, attrs)

        # Create the resulting class.
        new_class = super(TaskMeta, cls).__new__(cls, name, bases, attrs)

        # Verify that a _run method is present and raise TypeError otherwise.
        if not hasattr(new_class, '_run') or not callable(new_class._run):
            raise TypeError('Task subclass must define a _run method.')

        # Return the new class object.
        return new_class


class Task2(object):
    """
    An abstract class representing a task that must run, 
    and which should track individual runs and results.
    """
    abstract = True

    def __init__(self):
        self.runs = []

    def run(self):
        start = datetime.now()
        result = self._run()
        end = datetime.now()
        self.runs.append({
            'start': start,
            'end': end,
            'result': result,
        })
        return result

# ------------------------------------------------------------------


class Task3(object):
    """
    An abstract class representing a task that must run, 
    and which should track individual runs and results.
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.runs = []

    def run(self):
        start = datetime.now()
        result = self._run()
        end = datetime.now()
        self.runs.append({
            'start': start,
            'end': end,
            'result': result,
        })
        return result

    @abc.abstractmethod
    def _run(self):
        pass
