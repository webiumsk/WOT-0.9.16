# 2016.10.11 22:20:37 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Lib/json/tests/__init__.py
import os
import sys
import json
import doctest
import unittest
from test import test_support
cjson = test_support.import_fresh_module('json', fresh=['_json'])
pyjson = test_support.import_fresh_module('json', blocked=['_json'])

class PyTest(unittest.TestCase):
    json = pyjson
    loads = staticmethod(pyjson.loads)
    dumps = staticmethod(pyjson.dumps)


@unittest.skipUnless(cjson, 'requires _json')

class CTest(unittest.TestCase):
    if cjson is not None:
        json = cjson
        loads = staticmethod(cjson.loads)
        dumps = staticmethod(cjson.dumps)


class TestPyTest(PyTest):

    def test_pyjson(self):
        self.assertEqual(self.json.scanner.make_scanner.__module__, 'json.scanner')
        self.assertEqual(self.json.decoder.scanstring.__module__, 'json.decoder')
        self.assertEqual(self.json.encoder.encode_basestring_ascii.__module__, 'json.encoder')


class TestCTest(CTest):

    def test_cjson(self):
        self.assertEqual(self.json.scanner.make_scanner.__module__, '_json')
        self.assertEqual(self.json.decoder.scanstring.__module__, '_json')
        self.assertEqual(self.json.encoder.c_make_encoder.__module__, '_json')
        self.assertEqual(self.json.encoder.encode_basestring_ascii.__module__, '_json')


here = os.path.dirname(__file__)

def test_suite():
    suite = additional_tests()
    loader = unittest.TestLoader()
    for fn in os.listdir(here):
        if fn.startswith('test') and fn.endswith('.py'):
            modname = 'json.tests.' + fn[:-3]
            __import__(modname)
            module = sys.modules[modname]
            suite.addTests(loader.loadTestsFromModule(module))

    return suite


def additional_tests():
    suite = unittest.TestSuite()
    for mod in (json, json.encoder, json.decoder):
        suite.addTest(doctest.DocTestSuite(mod))

    suite.addTest(TestPyTest('test_pyjson'))
    suite.addTest(TestCTest('test_cjson'))
    return suite


def main():
    suite = test_suite()
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    main()
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\json\tests\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:20:37 St�edn� Evropa (letn� �as)
