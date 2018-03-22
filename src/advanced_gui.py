#!/bin/env python3

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from gui import gui
from gui_step import GUIStep
from vconsole_lib import vconsole_lib
from vm_lib import vm_lib


class AdvancedGUI(GUIStep):
    def __init__(self):
        gui.builder.get_object('spinbutton_vm').set_value(
            vm_lib.get_swappiness())
        gui.builder.get_object('spinbutton_vm').connect(
            'value-changed', self._vm_swappiness_changed)
        gui.builder.get_object('button_vm_reset').connect(
            'clicked', self._vm_swappiness_reset_clicked)
        gui.builder.get_object('entry_font').set_text(vconsole_lib.get_font())
        gui.builder.get_object('entry_font').connect(
            'changed', self._font_changed)
        gui.builder.get_object('button_font_reset').connect(
            'clicked', self._font_reset_clicked)
        gui.builder.get_object('entry_keymap').set_text(
            vconsole_lib.get_keymap())
        gui.builder.get_object('entry_keymap').connect(
            'changed', self._keymap_changed)
        gui.builder.get_object('button_keymap_reset').connect(
            'clicked', self._keymap_reset_clicked)

    def update_text(self):
        gui.builder.get_object('label_vm').set_label(_('VM Swappiness'))
        gui.builder.get_object('label_vm_swapping').set_label(_(
            'Note: On modern computers with large memory, VM swapping can ' +
            'slow the system down or even freeze the entire computer. Set ' +
            'the value to 0 to disable swapping (does not affect hibernation)' +
            '.' +
            '\n\n' +
            'You can edit this value later in /etc/sysctl.d/99-sysctl.conf.'
        ))
        gui.builder.get_object('button_vm_reset').set_label(_('Reset'))
        gui.builder.get_object('label_vconsole').set_label(_('Virtual Console'))
        gui.builder.get_object('label_vconsole_font').set_label(_('Font'))
        gui.builder.get_object('button_font_reset').set_label(_('Reset'))
        gui.builder.get_object('label_vconsole_keymap').set_label(_(
            'Keyboard Mapping'))
        gui.builder.get_object('button_keymap_reset').set_label(_('Reset'))
        gui.builder.get_object('label_vconsole_notice').set_label(_(
            'You can edit these values later in /etc/vconsole.conf.'))
        gui.builder.get_object('label_advanced').set_label(_('Advanced'))
        gui.builder.get_object('label_advanced_notice').set_label(
            _('Edit these options only when you are familiar with them.'))

    def _vm_swappiness_changed(self, spinbutton):
        vm_lib.set_swappiness(spinbutton.get_value())

    def _vm_swappiness_reset_clicked(self, button):
        gui.builder.get_object('spinbutton_vm').set_value(
            vm_lib.default_swappiness)

    def _font_changed(self, entry):
        vconsole_lib.set_font(entry.get_text())

    def _font_reset_clicked(self, button):
        gui.builder.get_object('entry_font').set_text('')

    def _keymap_changed(self, entry):
        vconsole_lib.set_keymap(entry.get_text())

    def _keymap_reset_clicked(self, button):
        gui.builder.get_object('entry_keymap').set_text('')


advanced_gui = AdvancedGUI()
