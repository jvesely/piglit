# Copyright (c) 2014, 2015 Intel Corporation

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

""" Module providing tests for the core module """


from __future__ import print_function, absolute_import

import nose.tools as nt

from framework import results, status, exceptions, grouptools
import framework.tests.utils as utils


@utils.nose_generator
def test_generate_initialize():
    """ Generator that creates tests to initialize all of the classes in core

    In a compiled language the compiler provides this kind of checking, but in
    an interpreted language like python you don't have a compiler test. The
    unit tests generated by this function serve as a similar test, does this
    even work?

    """
    @utils.no_error
    def check(target):
        target()

    for target in [results.TestrunResult, results.TestResult]:
        check.description = \
            "results.{}: class initializes".format(target.__name__)
        yield check, target


def test_Subtests_convert():
    """results.Subtests.__setitem__: converts strings to statues"""
    test = results.Subtests()
    test['foo'] = 'pass'
    nt.assert_is(test['foo'], status.PASS)


def test_Subtests_to_json():
    """results.Subtests.to_json: sets values properly"""
    baseline = {
        'foo': status.PASS,
        'bar': status.CRASH,
        '__type__': 'Subtests',
    }

    test = results.Subtests()
    test['foo'] = status.PASS
    test['bar'] = status.CRASH

    nt.eq_(baseline, test.to_json())


def test_Subtests_from_dict():
    """results.Subtests.from_dict: restores values properly"""
    baseline = results.Subtests()
    baseline['foo'] = status.PASS
    baseline['bar'] = status.CRASH

    test = results.Subtests.from_dict(baseline.to_json())

    nt.assert_dict_equal(baseline, test)


def test_Subtests_from_dict_instance():
    """results.Subtests.from_dict: restores values properly"""
    baseline = results.Subtests()
    baseline['foo'] = status.PASS

    test = results.Subtests.from_dict(baseline.to_json())

    nt.assert_is(test['foo'], status.PASS)


def test_TestResult_from_dict_inst():
    """results.TestResult.from_dict: returns a TestResult"""
    test = results.TestResult.from_dict({'result': 'pass'})
    nt.ok_(isinstance(test, results.TestResult))


class TestTestResultFromDictAttributes(object):
    """A series of tests to show that each attribute is sucessfully populated.
    """
    @classmethod
    def setup_class(cls):
        dict_ = {
            'returncode': 10,
            'err': 'stderr',
            'out': 'stdout',
            'time': 1.2345,
            'command': 'this is a command',
            'environment': 'environment variables',
            'result': 'pass',
            'dmesg': 'this is some dmesg',
        }

        cls.test = results.TestResult.from_dict(dict_)

    def test_returncode(self):
        """results.TestResult.from_dict: sets returncode correctly"""
        nt.eq_(self.test.returncode, 10)

    def test_err(self):
        """results.TestResult.from_dict: sets err correctly"""
        nt.eq_(self.test.err, 'stderr')

    def test_out(self):
        """results.TestResult.from_dict: sets out correctly"""
        nt.eq_(self.test.out, 'stdout')

    def test_time(self):
        """results.TestResult.from_dict: sets time correctly"""
        nt.eq_(self.test.time, 1.2345)

    def test_command(self):
        """results.TestResult.from_dict: sets command correctly"""
        nt.eq_(self.test.command, 'this is a command')

    def test_environment(self):
        """results.TestResult.from_dict: sets environment correctly"""
        nt.eq_(self.test.environment, 'environment variables')

    def test_result(self):
        """results.TestResult.from_dict: sets result correctly"""
        nt.eq_(self.test.result, 'pass')

    def test_dmesg(self):
        """dmesgs.TestResult.from_dict: sets dmesg correctly"""
        nt.eq_(self.test.dmesg, 'this is some dmesg')


def test_TestResult_result_getter():
    """results.TestResult.result: Getter returns the result when there are no subtests"""
    test = results.TestResult('pass')
    nt.eq_(test.result, 'pass')


def test_TestResult_result_getter_subtests():
    """results.TestResult.result: Getter returns worst subtest when subtests are present"""
    test = results.TestResult('pass')
    test.subtests['a'] = 'fail'
    test.subtests['b'] = 'crash'
    test.subtests['c'] = 'incomplete'
    nt.eq_(test.result, 'incomplete')


def test_TestResult_result_setter():
    """results.TestResult.result: setter makes the result a status"""
    test = results.TestResult('pass')
    test.result = 'fail'
    nt.ok_(isinstance(test.result, status.Status))
    nt.eq_(test.result, 'fail')


@nt.raises(exceptions.PiglitFatalError)
def test_TestResult_result_setter_invalid():
    """results.TestResult.result: setter raises PiglitFatalError for invalid values"""
    test = results.TestResult('pass')
    test.result = 'poop'


class TestTestResult_to_json(object):
    """Tests for the attributes of the to_json method."""
    @classmethod
    def setup_class(cls):
        cls.dict = {
            'returncode': 100,
            'err': 'this is an err',
            'out': 'this is some text',
            'time': 0.5,
            'environment': 'some env stuff',
            'subtests': {
                'a': 'pass',
                'b': 'fail',
            },
            'result': 'crash',
            'exception': 'an exception',
        }

        test = results.TestResult.from_dict(cls.dict)

        cls.json = test.to_json()

    def test_returncode(self):
        """results.TestResult.to_json: sets the returncode correctly"""
        nt.eq_(self.dict['returncode'], self.json['returncode'])

    def test_err(self):
        """results.TestResult.to_json: sets the err correctly"""
        nt.eq_(self.dict['err'], self.json['err'])

    def test_out(self):
        """results.TestResult.to_json: sets the out correctly"""
        nt.eq_(self.dict['out'], self.json['out'])

    def test_exception(self):
        """results.TestResult.to_json: sets the exception correctly"""
        nt.eq_(self.dict['exception'], self.json['exception'])

    def test_time(self):
        """results.TestResult.to_json: sets the time correctly"""
        nt.eq_(self.dict['time'], self.json['time'])

    def test_environment(self):
        """results.TestResult.to_json: sets the environment correctly"""
        nt.eq_(self.dict['environment'], self.json['environment'])

    def test_subtests(self):
        """results.TestResult.to_json: sets the subtests correctly"""
        nt.eq_(self.dict['subtests'], self.json['subtests'])

    def test_type(self):
        """results.TestResult.to_json: adds the __type__ hint"""
        nt.eq_(self.json['__type__'], 'TestResult')


class TestTestResult_from_dict(object):
    """Tests for the from_dict method."""
    @classmethod
    def setup_class(cls):
        cls.dict = {
            'returncode': 100,
            'err': 'this is an err',
            'out': 'this is some text',
            'time': 0.5,
            'environment': 'some env stuff',
            'subtests': {
                'a': 'pass',
                'b': 'fail',
            },
            'result': 'crash',
            'exception': 'an exception',
        }

        cls.test = results.TestResult.from_dict(cls.dict)

    def test_returncode(self):
        """results.TestResult.from_dict: sets returncode properly"""
        nt.eq_(self.test.returncode, self.dict['returncode'])

    def test_err(self):
        """results.TestResult.from_dict: sets err properly"""
        nt.eq_(self.test.err, self.dict['err'])

    def test_out(self):
        """results.TestResult.from_dict: sets out properly"""
        nt.eq_(self.test.out, self.dict['out'])

    def test_time(self):
        """results.TestResult.from_dict: sets time properly"""
        nt.eq_(self.test.time, self.dict['time'])

    def test_environment(self):
        """results.TestResult.from_dict: sets environment properly"""
        nt.eq_(self.test.environment, self.dict['environment'])

    def test_exception(self):
        """results.TestResult.from_dict: sets exception properly"""
        nt.eq_(self.test.exception, self.dict['exception'])

    def test_subtests(self):
        """results.TestResult.from_dict: sets subtests properly"""
        nt.eq_(self.test.subtests, self.dict['subtests'])

    def test_subtests_type(self):
        """results.TestResult.from_dict: subtests are Status instances"""
        nt.assert_is(self.test.subtests['a'], status.PASS)
        nt.assert_is(self.test.subtests['b'], status.FAIL)


def test_TestResult_update():
    """results.TestResult.update: result is updated"""
    test = results.TestResult('pass')
    test.update({'result': 'incomplete'})
    nt.eq_(test.result, 'incomplete')


def test_TestResult_update_subtests():
    """results.TestResult.update: subests are updated"""
    test = results.TestResult('pass')
    test.update({'subtest': {'result': 'incomplete'}})
    nt.eq_(test.subtests['result'], 'incomplete')


class TestStringDescriptor(object):
    """Test class for StringDescriptor."""
    @classmethod
    def setup_class(cls):
        class Test(object):  # pylint: disable=too-few-public-methods
            val = results.StringDescriptor('test')

        cls.class_ = Test

    def setup(self):
        self.test = self.class_()

    def test_get_default(self):
        """results.StringDescriptor.__get__: returns default when unset"""
        nt.eq_(self.test.val, u'')

    def test_set_no_replace(self):
        """results.StringDescriptor.__set__: instance is not replaced

        This test might not make sense if you don't understand the difference
        between 'is' and '==' in python. '==' is an equavalency test, while
        'is' returns true only if the instances are the same.

        What this test does is makes sure that self.test.val is not *replaced*
        by inst, and instead the value is passed into the __set__ method.

        """
        inst = 'foo'
        self.test.val = inst
        nt.ok_(self.test.val is not inst)

    def test_set_unicode(self):
        """results.StringDescriptor.__set__: unicode is stored directly"""
        inst = u'foo'
        self.test.val = inst
        nt.eq_(self.test.val, inst)

    def test_set_str(self):
        """results.StringDescriptor.__set__: converts strs to unicode"""
        inst = 'foo'
        self.test.val = inst
        nt.eq_(self.test.val, unicode(inst))

    @utils.no_error
    def test_set_str_unicode_literals(self):
        """results.StringDescriptor.__set__: handles unicode litterals in strs
        """
        inst = r'\ufffd'
        self.test.val = inst

    @nt.raises(NotImplementedError)
    def test_delete(self):
        """results.StringDescriptor.__delete__: raises NotImplementedError"""
        del self.test.val


class TestTestrunResultTotals(object):
    """Test the totals generated by TestrunResult.calculate_group_totals()."""
    @classmethod
    def setup_class(cls):
        pass_ = results.TestResult('pass')
        fail = results.TestResult('fail')
        #warn = results.TestResult('warn')
        crash = results.TestResult('crash')
        skip = results.TestResult('skip')
        tr = results.TestrunResult()
        tr.tests = {
            'oink': pass_,
            grouptools.join('foo', 'bar'): fail,
            grouptools.join('foo', 'foo', 'bar'): crash,
            grouptools.join('foo', 'foo', 'oink'): skip,
        }

        tr.calculate_group_totals()
        cls.test = tr.totals

    def test_root(self):
        """results.TestrunResult.totals: The root is correct"""
        root = results.Totals()
        root['pass'] += 1
        root['fail'] += 1
        root['crash'] += 1
        root['skip'] += 1

        nt.assert_dict_equal(self.test['root'], root)

    def test_recurse(self):
        """results.TestrunResult.totals: Recurses correctly"""
        expected = results.Totals()
        expected['fail'] += 1
        expected['crash'] += 1
        expected['skip'] += 1
        nt.assert_dict_equal(self.test['foo'], expected)

    def test_two_parents(self):
        """results.TestrunResult.totals: Handles multiple parents correctly"""
        expected = results.Totals()
        expected['crash'] += 1
        expected['skip'] += 1
        nt.assert_dict_equal(self.test[grouptools.join('foo', 'foo')], expected)


class TestTestrunResultTotalsSubtests(object):
    """results.TestrunResult.totals: Tests with subtests are handled correctly"""
    @classmethod
    def setup_class(cls):
        tr = results.TestResult('crash')
        tr.subtests['foo'] = status.PASS
        tr.subtests['bar'] = status.CRASH
        tr.subtests['oink'] = status.FAIL

        run = results.TestrunResult()
        run.tests[grouptools.join('sub', 'test')] = tr
        run.calculate_group_totals()

        cls.test = run.totals

    def test_root(self):
        """results.TestrunResult.totals: The root is correct with subtests"""
        expect = results.Totals()
        expect['pass'] += 1
        expect['crash'] += 1
        expect['fail'] += 1
        nt.assert_dict_equal(self.test['root'], expect)

    def test_node(self):
        """results.TestrunResult.totals: Tests with subtests are treated as groups"""
        key = grouptools.join('sub', 'test')
        nt.ok_(key in self.test,
               msg='Key: {} not found in {}'.format(key, self.test.keys()))

    def test_node_values(self):
        """results.TestrunResult.totals: Tests with subtests values are correct"""
        expect = results.Totals()
        expect['pass'] += 1
        expect['crash'] += 1
        expect['fail'] += 1
        nt.assert_dict_equal(self.test[grouptools.join('sub', 'test')], expect)


def test_totals_false():
    """results.Totals: bool() returns False when all values are 0"""
    nt.ok_(not bool(results.Totals()))


def test_totals_true():
    """results.Totals: bool() returns True when any value is not 0"""
    # This might deserve a generator, but it seems so simple that it it's a lot
    # of work for no gain
    for key in results.Totals().iterkeys():
        test = results.Totals()
        test[key] += 1
        nt.ok_(bool(test), msg='Returns false with status {}'.format(key))


class TestTestrunResultToJson(object):
    """results.TestrunResult.to_json: returns expected values"""
    @classmethod
    def setup_class(cls):
        test = results.TestrunResult()
        test.name = 'name'
        test.uname = 'this is uname'
        test.options = {'some': 'option'}
        test.glxinfo = 'glxinfo'
        test.clinfo = 'clinfo'
        test.wglinfo = 'wglinfo'
        test.lspci = 'this is lspci'
        test.time_elapsed.end = 1.23
        test.tests = {'a test': results.TestResult('pass')}

        cls.test = test.to_json()

    def test_name(self):
        """results.TestrunResult.to_json: name is properly encoded"""
        nt.eq_(self.test['name'], 'name')

    def test_uname(self):
        """results.TestrunResult.to_json: uname is properly encoded"""
        nt.eq_(self.test['uname'], 'this is uname')

    def test_options(self):
        """results.TestrunResult.to_json: options is properly encoded"""
        nt.assert_dict_equal(self.test['options'], {'some': 'option'})

    def test_glxinfo(self):
        """results.TestrunResult.to_json: glxinfo is properly encoded"""
        nt.eq_(self.test['glxinfo'], 'glxinfo')

    def test_wglinfo(self):
        """results.TestrunResult.to_json: wglinfo is properly encoded"""
        nt.eq_(self.test['wglinfo'], 'wglinfo')

    def test_clinfo(self):
        """results.TestrunResult.to_json: clinfo is properly encoded"""
        nt.eq_(self.test['clinfo'], 'clinfo')

    def test_lspci(self):
        """results.TestrunResult.to_json: lspci is properly encoded"""
        nt.eq_(self.test['lspci'], 'this is lspci')

    def test_time(self):
        """results.TestrunResult.to_json: time_elapsed is properly encoded"""
        nt.eq_(self.test['time_elapsed'].end, 1.23)

    def test_tests(self):
        """results.TestrunResult.to_json: tests is properly encoded"""
        nt.eq_(self.test['tests']['a test'].result, 'pass')

    def test_type(self):
        """results.TestrunResult.to_json: __type__ is added"""
        nt.eq_(self.test['__type__'], 'TestrunResult')


class TestTestrunResultFromDict(object):
    """Tests for TestrunResult.from_dict."""
    @classmethod
    def setup_class(cls):
        subtest = results.TestResult('fail')
        subtest.subtests['foo'] = 'pass'

        test = results.TestrunResult()
        test.name = 'name'
        test.uname = 'this is uname'
        test.options = {'some': 'option'}
        test.glxinfo = 'glxinfo'
        test.wglinfo = 'wglinfo'
        test.clinfo = 'clinfo'
        test.lspci = 'this is lspci'
        test.time_elapsed.end = 1.23
        test.tests = {
            'a test': results.TestResult('pass'),
            'subtest': subtest,
        }
        test.results_version = 100000  # This will never be less than current

        cls.baseline = test
        cls.test = results.TestrunResult.from_dict(test.to_json())

    @utils.nose_generator
    def test_basic(self):
        """Generate tests for basic attributes"""

        def test(baseline, test):
            nt.eq_(baseline, test)

        for attrib in ['name', 'uname', 'glxinfo', 'wglinfo', 'lspci',
                       'results_version', 'clinfo']:
            test.description = ('results.TestrunResult.from_dict: '
                                '{} is restored correctly'.format(attrib))
            yield (test,
                   getattr(self.baseline, attrib),
                   getattr(self.test, attrib))

    def test_tests(self):
        """results.TestrunResult.from_dict: tests is restored correctly"""
        nt.eq_(self.test.tests['a test'].result,
               self.baseline.tests['a test'].result)

    def test_test_type(self):
        """results.TestrunResult.from_dict: tests is restored correctly"""
        nt.ok_(isinstance(self.test.tests['a test'].result, status.Status),
               msg='Tests should be type Status, but was "{}"'.format(
                   type(self.test.tests['a test'].result)))

    def test_totals(self):
        """results.TestrunResult.from_dict: totals is restored correctly"""
        nt.assert_dict_equal(self.baseline.totals, self.test.totals)

    def test_subtests(self):
        """results.TestrunResult.from_dict: subtests are restored correctly"""
        nt.eq_(self.test.tests['subtest'].subtests['foo'],
               self.baseline.tests['subtest'].subtests['foo'])

    def test_subtest_type(self):
        """results.TestrunResult.from_dict: subtests are Status instances"""
        nt.ok_(isinstance(self.test.tests['subtest'].subtests['foo'],
                          status.Status),
               msg='Subtests should be type Status, but was "{}"'.format(
                   type(self.test.tests['subtest'].subtests['foo'])))

    def test_time_elapsed(self):
        """results.TestrunRresult.from_dict: time_elapsed is restored correctly
        """
        nt.eq_(self.baseline.time_elapsed.end, self.test.time_elapsed.end)

    def test_time(self):
        """results.TestrunResult.from_dict: time_elapsed is TimeAttribute instance"""
        nt.ok_(isinstance(self.test.time_elapsed, results.TimeAttribute),
               msg='time_elapsed should be tpe TimeAttribute, '
                   'but was "{}"'.format(type(self.test.time_elapsed)))


def test_TimeAttribute_to_json():
    """results.TimeAttribute.to_json(): returns expected dictionary"""
    baseline = {'start': 0.1, 'end': 1.0}
    test = results.TimeAttribute(**baseline)
    baseline['__type__'] = 'TimeAttribute'

    nt.assert_dict_equal(baseline, test.to_json())


def test_TimeAttribute_from_dict():
    """results.TimeAttribute.from_dict: returns expected value"""
    # Type is included because to_json() adds it.
    baseline = {'start': 0.1, 'end': 1.0, '__type__': 'TimeAttribute'}
    test = results.TimeAttribute.from_dict(baseline).to_json()

    nt.assert_dict_equal(baseline, test)


def test_TimeAttribute_total():
    """results.TimeAttribute.total: returns the difference between end and start"""
    test = results.TimeAttribute(1.0, 5.0)
    nt.eq_(test.total, 4.0)


def test_TimeAttribute_delta():
    """results.TimeAttribute.delta: returns the delta of the values"""
    test = results.TimeAttribute(1.0, 5.0)
    nt.eq_(test.delta, '0:00:04')
