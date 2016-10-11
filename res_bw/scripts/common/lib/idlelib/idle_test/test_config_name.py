# 2016.10.11 22:20:32 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Lib/idlelib/idle_test/test_config_name.py
"""Unit tests for idlelib.configSectionNameDialog"""
import unittest
from idlelib.idle_test.mock_tk import Var, Mbox
from idlelib import configSectionNameDialog as name_dialog_module
name_dialog = name_dialog_module.GetCfgSectionNameDialog

class Dummy_name_dialog(object):
    name_ok = name_dialog.name_ok.im_func
    Ok = name_dialog.Ok.im_func
    Cancel = name_dialog.Cancel.im_func
    used_names = ['used']
    name = Var()
    result = None
    destroyed = False

    def destroy(self):
        self.destroyed = True


orig_mbox = name_dialog_module.tkMessageBox
showerror = Mbox.showerror

class ConfigNameTest(unittest.TestCase):
    dialog = Dummy_name_dialog()

    @classmethod
    def setUpClass(cls):
        name_dialog_module.tkMessageBox = Mbox

    @classmethod
    def tearDownClass(cls):
        name_dialog_module.tkMessageBox = orig_mbox

    def test_blank_name(self):
        self.dialog.name.set(' ')
        self.assertEqual(self.dialog.name_ok(), '')
        self.assertEqual(showerror.title, 'Name Error')
        self.assertIn('No', showerror.message)

    def test_used_name(self):
        self.dialog.name.set('used')
        self.assertEqual(self.dialog.name_ok(), '')
        self.assertEqual(showerror.title, 'Name Error')
        self.assertIn('use', showerror.message)

    def test_long_name(self):
        self.dialog.name.set('good' * 8)
        self.assertEqual(self.dialog.name_ok(), '')
        self.assertEqual(showerror.title, 'Name Error')
        self.assertIn('too long', showerror.message)

    def test_good_name(self):
        self.dialog.name.set('  good ')
        showerror.title = 'No Error'
        self.assertEqual(self.dialog.name_ok(), 'good')
        self.assertEqual(showerror.title, 'No Error')

    def test_ok(self):
        self.dialog.destroyed = False
        self.dialog.name.set('good')
        self.dialog.Ok()
        self.assertEqual(self.dialog.result, 'good')
        self.assertTrue(self.dialog.destroyed)

    def test_cancel(self):
        self.dialog.destroyed = False
        self.dialog.Cancel()
        self.assertEqual(self.dialog.result, '')
        self.assertTrue(self.dialog.destroyed)


if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\idlelib\idle_test\test_config_name.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:20:32 St�edn� Evropa (letn� �as)