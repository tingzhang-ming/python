from abc import ABCMeta, abstractmethod


class LiftState(object):

    __metaclass__ = ABCMeta

    def __init__(self):
        self._context = None

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, val):
        self._context = val

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def stop(self):
        pass

#################################


class OpenningState(LiftState):

    def close(self):
        self.context.lift_state = Context.closing_state
        self.context.lift_state.close()

    def open(self):
        print "lift open..."

    def run(self):
        pass

    def stop(self):
        pass


#################################


class ClosingState(LiftState):

    def close(self):
        print "lift close"

    def open(self):
        self.context.lift_state = Context.opening_state
        self.context.lift_state.open()

    def run(self):
        self.context.lift_state = Context.running_state
        self.context.lift_state.run()

    def stop(self):
        self.context.lift_state = Context.stopping_state
        self.context.lift_state.stop()


#################################


class RunningState(LiftState):
    def close(self):
        pass

    def open(self):
        pass

    def run(self):
        print "lift run up and down"

    def stop(self):
        self.context.lift_state = Context.stopping_state
        self.context.lift_state.stop()


#################################


class StoppingState(LiftState):

    def close(self):
        pass

    def open(self):
        self.context.lift_state = Context.opening_state
        self.context.lift_state.open()

    def run(self):
        self.context.lift_state = Context.running_state
        self.context.lift_state.run()

    def stop(self):
        print "lift stop"


#########################################


class Context(object):
    opening_state = OpenningState()
    closing_state = ClosingState()
    running_state = RunningState()
    stopping_state = StoppingState()

    def __init__(self):
        self._lift_state = None

    @property
    def lift_state(self):
        return self._lift_state

    @lift_state.setter
    def lift_state(self, val):
        self._lift_state = val
        self._lift_state.context = self

    def open(self):
        self._lift_state.open()

    def close(self):
        self._lift_state.close()

    def run(self):
        self._lift_state.run()

    def stop(self):
        self._lift_state.stop()


if __name__ == '__main__':
    context = Context()
    context.lift_state = ClosingState()
    context.open()
    context.close()
    context.run()
    context.stop()
# lift open...
# lift close
# lift run up and down
# lift stop
