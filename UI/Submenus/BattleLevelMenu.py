from PySide6.QtWidgets import QHBoxLayout, QGridLayout, QWidget, QLabel

from Class import settingkey
from Class.seedSettings import SeedSettings
from List.configDict import locationType
from UI.Submenus.SubMenu import KH2Submenu
from Module.battleLevels import BtlvViewer

class BattleLevelMenu(KH2Submenu):
    def __init__(self, settings: SeedSettings):
        super().__init__(title='World Battle Levels', settings=settings, in_layout='horizontal')
        self.world_level_labels = {}
        self.battle_levels = BtlvViewer()

        self.start_column()
        self.addHeader("Options")
        self.add_option(settingkey.BATTLE_LEVEL_RANDO)
        self.add_option(settingkey.BATTLE_LEVEL_OFFSET)
        self.end_column()

        self.start_column()
        self.addHeader("Battle Levels")
        self.full_world_level_layout = QGridLayout()
        first_label = QLabel("1st")
        second_label = QLabel("2nd")
        third_label = QLabel("3rd")
        self.full_world_level_layout.addWidget(first_label,0,1)
        self.full_world_level_layout.addWidget(second_label,0,2)
        self.full_world_level_layout.addWidget(third_label,0,3)
        self.add_battle_level_info(locationType.STT,1)
        self.add_battle_level_info(locationType.TT,3)
        self.add_battle_level_info(locationType.HB,2)
        self.add_battle_level_info(locationType.LoD,2)
        self.add_battle_level_info(locationType.BC,2)
        self.add_battle_level_info(locationType.OC,2)
        self.add_battle_level_info(locationType.DC,1)
        self.add_battle_level_info(locationType.PR,2)
        self.add_battle_level_info(locationType.Agrabah,2)
        self.add_battle_level_info(locationType.HT,2)
        self.add_battle_level_info(locationType.PL,2)
        self.add_battle_level_info(locationType.SP,2)
        self.add_battle_level_info(locationType.TWTNW,1)
        world_widget = QWidget()
        world_widget.setLayout(self.full_world_level_layout)
        self.pending_column.addWidget(world_widget)
        self.end_column()

        settings.observe(settingkey.BATTLE_LEVEL_RANDO, self._btlv_setting_change)
        settings.observe(settingkey.BATTLE_LEVEL_OFFSET, self._btlv_setting_change)

        self.finalizeMenu()

    def _btlv_setting_change(self):
        btlv_setting = self.settings.get(settingkey.BATTLE_LEVEL_RANDO)
        btlv_offset = self.settings.get(settingkey.BATTLE_LEVEL_OFFSET)
        self.set_option_visibility(settingkey.BATTLE_LEVEL_OFFSET, visible=(btlv_setting=="Offset"))

        self.update_battle_level_display(btlv_setting,btlv_offset)

    def update_battle_level_display(self,setting_name,btlv_offset):
        self.battle_levels.use_setting(setting_name,btlv_offset)
        for world,label_list in self.world_level_labels.items():
            for x in range(len(label_list)):
                label_list[x].setText(str(self.battle_levels.get_battle_levels(world)[x]))
        

    def add_battle_level_info(self,world,visits=1):
        world_label = QLabel(world.value)
        self.world_level_labels[world] = []
        world_row = len(self.world_level_labels)
        self.full_world_level_layout.addWidget(world_label,world_row,0)

        for x in range(visits):
            world_level_label = QLabel(str(self.battle_levels.get_battle_levels(world)[x]))
            self.full_world_level_layout.addWidget(world_level_label,world_row,1+x)
            self.world_level_labels[world].append(world_level_label)