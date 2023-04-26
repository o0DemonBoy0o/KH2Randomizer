class modYml:
    retryDarkThorn = "retryDarkThorn"
    retryDataXemnas = "retryDataXemnas"

    def getDefaultMod():
        return {
            "title": "Randomizer Seed",
            "assets": [
                #{
                #    "name": "msg/us/sys.bar",
                #    "multi": [
                #        {"name": "msg/fr/sys.bar"},
                #        {"name": "msg/gr/sys.bar"},
                #        {"name": "msg/it/sys.bar"},
                #        {"name": "msg/sp/sys.bar"},
                #    ],
                #    "method": "binarc",
                #    "source": [
                #        {
                #            "name": "sys",
                #            "type": "list",
                #            "method": "kh2msg",
                #            "source": [
                #                {
                #                    "name": "sys.yml",
                #                    "language": "en"
                #                }
                #            ]
                #        }
                #    ]
                #},
                #{
                #    "name": "msg/jp/sys.bar",
                #    "platform": "ps2",
                #    "method": "binarc",
                #    "source": [
                #        {
                #            "name": "sys",
                #            "type": "list",
                #            "method": "kh2msg",
                #            "source": [
                #                {
                #                    "name": "sys.yml",
                #                    "language": "en"
                #                }
                #            ]
                #        }
                #    ]
                #},
                #{
                #    "name": "msg/jp/sys.bar",
                #    "platform": "pc",
                #    "method": "binarc",
                #    "source": [
                #        {
                #            "name": "sys",
                #            "type": "list",
                #            "method": "kh2msg",
                #            "source": [
                #                {
                #                    "name": "sys.yml",
                #                    "language": "jp"
                #                }
                #            ]
                #        }
                #    ]
                #},
                #{
                #    "name": "00battle.bin",
                #    "method": "binarc",
                #    "source": [
                #        {
                #            "name": "fmlv",
                #            "method": "listpatch",
                #            "type": "List",
                #            "source": [
                #                {
                #                    "name": "FmlvList.yml",
                #                    "type": "fmlv"
                #                }
                #            ]
                #        },
                #        {
                #            "name": "lvup",
                #            "method": "listpatch",
                #            "type": "List",
                #            "source": [
                #                {
                #                    "name": "LvupList.yml",
                #                    "type": "lvup"
                #                }
                #            ]
                #        },
                #        {
                #            "name": "bons",
                #            "method": "listpatch",
                #            "type": "List",
                #            "source": [
                #                {
                #                    "name": "BonsList.yml",
                #                    "type": "bons"
                #                }
                #            ]
                #        },
                #        {
                #            "name": "plrp",
                #            "method": "listpatch",
                #            "type": "List",
                #            "source": [
                #                {
                #                    "name": "PlrpList.yml",
                #                    "type": "plrp"
                #                }
                #            ]
                #        }
                #    ]
                #},
                #{
                #    "name": "03system.bin",
                #    "method": "binarc",
                #    "source": [
                #        {
                #            "name": "trsr",
                #            "method": "listpatch",
                #            "type": "List",
                #            "source": [
                #                {
                #                    "name": "TrsrList.yml",
                #                    "type": "trsr"
                #                }
                #            ]
                #        },
                #        {
                #            "name": "item",
                #            "method": "listpatch",
                #            "type": "List",
                #            "source": [
                #                {
                #                    "name": "ItemList.yml",
                #                    "type": "item"
                #                }
                #            ]
                #        }
                #    ]
                #}
            ]
        }

    def getSysYAML(seedHashIcons, crit_mode = False):
        seedHashString = " ".join(["{:icon " + icon + "}" for icon in seedHashIcons])
        sys = [{"id": 17198, "en":seedHashString, "jp":seedHashString}]
        # sys.append({"id": 19482, "en": "Important Checks Found"}) # Not needed until we figure out how to display the correct amount
        if crit_mode:
            sys.append({"id": 17201, "en": "{:color #FF000080}Beginner (WARNING)", "jp": "{:color #FF000080}ビギナーモード (注意!)"})
            sys.append({"id": 17202, "en": "{:color #FF000080}Standard (WARNING)", "jp": "{:color #FF000080}スタンダードモード (注意!)"})
            sys.append({"id": 17203, "en": "{:color #FF000080}Proud (WARNING)", "jp": "{:color #FF000080}プラウドモード (注意!)"})
            sys.append({
                "id": 17204,
                "en": "An easier mode for beginners.\n{:color #FF000080}Critical Bonuses are turned on. The seven\nrandom starting items will be unobtainable.",
                "jp": "敵が弱く サクサクすすめるかんたんモードです\n{:color #FF000080}クリティカル特典が有効になっていますが、このモード\nではゲーム開始時に7つの特典を受け取れません",
            })
            sys.append({
                "id": 17205,
                "en": "A balanced mode best for those challenging\nthis game for the first time.\n{:color #FF000080}Critical Bonuses are turned on. The seven\nrandom starting items will be unobtainable.",
                "jp": "初プレイにピッタリの ほどよいバランスのモードです\n{:color #FF000080}クリティカル特典が有効になっていますが、このモード\nではゲーム開始時に7つの特典を受け取れません",
            })
            sys.append({
                "id": 17206,
                "en": "A difficult mode with stronger enemies.\nBest for those seeking a challenge.\n{:color #FF000080}Critical Bonuses are turned on. The seven\nrandom starting items will be unobtainable.",
                "jp": "敵が強く スリリングなバトルがたのしめるモードです\n{:color #FF000080}クリティカル特典が有効になっていますが、このモード\nではゲーム開始時に7つの特典を受け取れません",
            })
            sys.append({
                "id": 20020,
                "en": "A true test of skill for the adept. Begin\nwith certain abilities and other perks.\n{:color #F0F00080}Critical Bonuses are turned on. The seven\nstarting items have been randomized.",
                "jp": "アクションのウデがためされる 上級者向けのモードです\n{:color #FF000080}クリティカル特典が有効になっています。ゲーム開始時\nにランダムな7つの特典を受け取れます",
            })
        else:
            sys.append({
                "id": 20020,
                "en": "A true test of skill for the adept. Begin\nwith certain abilities and other perks.\n{:color #F0F00080}Critical Bonuses are turned off. The seven\nstarting items will be junk.",
                "jp": "アクションのウデがためされる 上級者向けのモードです\n{:color #FF000080}クリティカル特典が無効になっています。ゲーム開始時\nにランダムな7つのジャンクアイテムを受け取れます",
            })

        return sys
    
    def getASDataMod():
        ASMod = []
        for ASRoom in ['hb32','hb33','hb34','hb38']:
            ASMod.append({
                "name": "ard/"+ASRoom+".ard",
                "multi": [
                    {"name": "ard/jp/"+ASRoom+".ard"},
                    {"name": "ard/us/"+ASRoom+".ard"},
                    {"name": "ard/fr/"+ASRoom+".ard"},
                    {"name": "ard/gr/"+ASRoom+".ard"},
                    {"name": "ard/it/"+ASRoom+".ard"},
                    {"name": "ard/sp/"+ASRoom+".ard"},
                ],
                "method": "binarc",
                "source": [
                    {
                        "name": "evt",
                        "type": "areadatascript",
                        "method": "areadatascript",
                        "source": [{"name": "asdata/"+ASRoom+"evt.script"}]
                    }
                ],
            })
        return ASMod
        
    def getPuzzleMod(pc = False):
        mod_dict = {
                    "method": "binarc",
                    "source": [
                        {
                            "name": "puzz",
                            "type": "jimidata",
                            "method": "copy",
                            "source": [
                                {
                                    "name": "modified_puzzle.bin"
                                }
                            ]
                        }
                    ]
                }

        mod_dict["name"] = "menu/fm/jiminy.bar"

        if pc:
            mod_dict["multi"] = [
                        {"name": "menu/us/jiminy.bar"},
                        {"name": "menu/fr/jiminy.bar"},
                        {"name": "menu/gr/jiminy.bar"},
                        {"name": "menu/it/jiminy.bar"},
                        {"name": "menu/sp/jiminy.bar"},
                        {"name": "menu/uk/jiminy.bar"},
                    ]

        return mod_dict

    def getDropMod():
        return  {
                    "name": "przt",
                    "type": "list",
                    "method": "copy",
                    "source": [
                        {
                            "name": "modified_drops.bin"
                        }
                    ]
                }
    def getDropModList():
        return  {
                    "name": "przt",
                    "type": "list",
                    "method": "listpatch",
                    "source": [
                        {
                            "name": "przt.yml",
                            "type": "przt"
                        }
                    ]
                }

    def getShopMod():
        return  {
                    "name": "shop",
                    "type": "unknown41",
                    "method": "copy",
                    "source": [
                        {
                            "name": "modified_shop.bin"
                        }
                    ]
                }

    def getSynthMod(pc=False):
        mod_dict = {
                    "method": "binarc",
                    "source": [
                        {
                            "name": "reci",
                            "type": "synthesis",
                            "method": "copy",
                            "source": [
                                {
                                    "name": "modified_synth.bin"
                                }
                            ]
                        },
                        {
                            "name": "cond",
                            "type": "synthesis",
                            "method": "copy",
                            "source": [
                                {
                                    "name": "modified_synth_reqs.bin"
                                }
                            ]
                        }
                    ]
                }
        mod_dict["name"] = "menu/fm/mixdata.bar"
        if pc:
            mod_dict["multi"] = [
                        {"name": "menu/us/mixdata.bar"},
                        {"name": "menu/fr/mixdata.bar"},
                        {"name": "menu/gr/mixdata.bar"},
                        {"name": "menu/it/mixdata.bar"},
                        {"name": "menu/sp/mixdata.bar"},
                        {"name": "menu/uk/mixdata.bar"},
                    ]
        return mod_dict
    def getSkipCarpetEscapeMod():
        return {
                "name": "ard/al11.ard",
                "multi": [
                    {"name": "ard/jp/al11.ard"},
                    {"name": "ard/us/al11.ard"},
                    {"name": "ard/fr/al11.ard"},
                    {"name": "ard/gr/al11.ard"},
                    {"name": "ard/it/al11.ard"},
                    {"name": "ard/sp/al11.ard"},
                ],
                "method": "binarc",
                "source": [
                    {
                        "name": "evt",
                        "type": "areadatascript",
                        "method": "areadatascript",
                        "source": [
                            {
                                "name": "skip_carpet_escape.script"
                            }
                        ]
                    }
                ]
            }


    def getBlockCorSkipMod():
        return {
                "name": "ard/hb24.ard",
                "multi": [
                    {"name": "ard/jp/hb24.ard"},
                    {"name": "ard/us/hb24.ard"},
                    {"name": "ard/fr/hb24.ard"},
                    {"name": "ard/gr/hb24.ard"},
                    {"name": "ard/it/hb24.ard"},
                    {"name": "ard/sp/hb24.ard"},
                ],
                "method": "binarc",
                "source": [
                    {
                        "name": "evt",
                        "type": "areadatascript",
                        "method": "areadatascript",
                        "source": [
                            {
                                "name": "disable_cor_skip.script"
                            }
                        ]
                    }
                ]
            }
            

    def getBlockShanYuSkipMod():
        return {
                "name": "ard/mu09.ard",
                "multi": [
                    {"name": "ard/jp/mu09.ard"},
                    {"name": "ard/us/mu09.ard"},
                    {"name": "ard/fr/mu09.ard"},
                    {"name": "ard/gr/mu09.ard"},
                    {"name": "ard/it/mu09.ard"},
                    {"name": "ard/sp/mu09.ard"},
                ],
                "method": "binarc",
                "source": [
                    {
                        "name": "evt",
                        "type": "areadatascript",
                        "method": "areadatascript",
                        "source": [
                            {
                                "name": "disable_shan_yu_skip.script"
                            }
                        ]
                    }
                ]
            }

    def getAtlanticaTutorialSkipMod():
        return {
                "name": "ard/lm02.ard",
                "multi": [
                    {"name": "ard/jp/lm02.ard"},
                    {"name": "ard/us/lm02.ard"},
                    {"name": "ard/fr/lm02.ard"},
                    {"name": "ard/gr/lm02.ard"},
                    {"name": "ard/it/lm02.ard"},
                    {"name": "ard/sp/lm02.ard"},
                ],
                "method": "binarc",
                "source": [
                    {
                        "name": "evt",
                        "type": "areadatascript",
                        "method": "areadatascript",
                        "source": [
                            {
                                "name": "atlantica_skip.script"
                            }
                        ]
                    }
                ]
            }

    def getWardrobeSkipMod():
        return {"name": "obj/N_BB080_BTL.mset","method": "copy","source": [{"name": "wardrobe_skip.mset"}]}


    def getMapSkipMod():
        return [
            {
                "name": "msg/us/ca.bar",
                "multi": [
                    {"name": "msg/fr/ca.bar"},
                    {"name": "msg/gr/ca.bar"},
                    {"name": "msg/it/ca.bar"},
                    {"name": "msg/sp/ca.bar"},
                ],
                "method": "binarc",
                "source": [
                    {
                        "name": "ca",
                        "type": "list",
                        "method": "kh2msg",
                        "source": [
                            {
                                "name": "map_skip/ca.yml",
                                "language": "en"
                            }
                        ]
                    }
                ]
            },
            {
                "name": "msg/jp/ca.bar",
                "platform": "ps2",
                "method": "binarc",
                "source": [
                    {
                        "name": "ca",
                        "type": "list",
                        "method": "kh2msg",
                        "source": [
                            {
                                "name": "map_skip/ca.yml",
                                "language": "en"
                            }
                        ]
                    }
                ]
            },
            {
                "name": "msg/jp/ca.bar",
                "platform": "pc",
                "method": "binarc",
                "source": [
                    {
                        "name": "ca",
                        "type": "list",
                        "method": "kh2msg",
                        "source": [
                            {
                                "name": "map_skip/ca.yml",
                                "language": "jp" # Change this to je whenever we update the mods manager
                            }
                        ]
                    }
                ]
            },
            {
                "name": "libretto-ca.bar",
                "method": "copy",
                "source": [
                    {
                        "name": "map_skip/libretto-ca.bar",
                    }
                ]
            },
        ]



    def getRetryMod(mod_choice):
        mod_names = {}
        mod_names[modYml.retryDarkThorn] = ("BB05_MS104B.bar","BB05","retry_dark_thorn.bin")
        mod_names[modYml.retryDataXemnas] = ("EH20_MS113_RE.bar","EH20","retry_data_xemnas.bin")
        return {
                    "name": "msn/jp/"+mod_names[mod_choice][0],
                    "multi": [
                        {"name": "msn/us/"+mod_names[mod_choice][0]},
                        {"name": "msn/fr/"+mod_names[mod_choice][0]},
                        {"name": "msn/gr/"+mod_names[mod_choice][0]},
                        {"name": "msn/it/"+mod_names[mod_choice][0]},
                        {"name": "msn/sp/"+mod_names[mod_choice][0]},
                    ],
                    "method": "binarc",
                    "source": [
                        {
                            "name": mod_names[mod_choice][1],
                            "type": "list",
                            "method": "copy",
                            "source": [
                                {
                                    "name": mod_names[mod_choice][2]
                                }
                            ]
                        }
                    ]
                }

    def getCmdListMod():
        return [{"method":"copy", "name":"cmd", "type":"list", "source":[{"name":"better_stt/cmd.list"}]}]

    def getBtlvMod():
        return [{"method":"copy", "name":"btlv", "type":"list", "source":[{"name":"modified_btlv.bin"}]}]

    def getBetterSTTMod(boss_enemy_enabled):
        return [{"name": "limit/fm/trinity_zz.bar","multi":[{"name":"limit/us/trinity_zz.bar"},{"name":"limit/fr/trinity_zz.bar"},{"name":"limit/gr/trinity_zz.bar"},{"name":"limit/it/trinity_zz.bar"},{"name":"limit/sp/trinity_zz.bar"}],"method": "copy","source": [{"name": "better_stt/trinity_zz.bar"}]},
                {"name": "obj/B_EX100.mset","method": "copy","source": [{"name": "better_stt/B_EX100.mset"}]},
                {"name": "obj/F_TT010.mset","method": "copy","source": [{"name": "better_stt/F_TT010.mset"}]},
                {"name": "obj/P_EX110.mset","method": "copy","source": [{"name": "better_stt/P_EX110.mset"}]},
                # {"name": "00objentry.bin","method": "listpatch","type": "List","source": [{"name": "better_stt/ObjList_Better_STT.yml", "type": "objentry"}]},
                {"name": "obj/W_EX010_RX.mset","method": "copy","source": [{"name": "better_stt/W_EX010_RX.mset"}]},] + \
                ([{"name": "obj/B_EX100_SR.mset","method": "copy","source": [{"name": "better_stt/B_EX100_SR.mset"}]},] if boss_enemy_enabled else [])

    def getChestVisualMod():
        ChestMod = []
        for ChestRoom1 in ['al00', 'al01', 'al06', 'al07', 'al10', 'al11', 'al12', 'al13', 
                       'bb02', 'bb03', 'bb06', 'bb07', 'bb08', 'bb09', 'bb10', 
                       'ca00', 'ca02', 'ca09', 'ca11', 'ca12', 'ca13', 'ca14', 'ca15', 
                       'dc01', 'dc03', 
                       'eh02', 'eh03', 'eh04', 'eh06', 'eh09', 'eh12', 'eh17', 
                       'hb03', 'hb09', 'hb11', 'hb12', 'hb18', 'hb21', 'hb22', 'hb23', 'hb24', 
                       'he03', 'he10', 'he11', 'he12', 'he15', 'he16', 'he17', 
                       'lk00', 'lk03', 'lk05', 'lk06', 'lk07', 'lk08', 'lk09', 
                       'mu00', 'mu02', 'mu03', 'mu05', 'mu06', 'mu11', 
                       'nm00', 'nm01', 'nm02', 'nm04', 'nm06', 'nm08', 
                       'po01', 'po02', 'po03', 'po04', 'po05', 'po09', 
                       'tr00', 'tr01', 'tr04', 'tr05', 'tr08', 
                       'wi00', 'wi01', 'wi02',
                       'tt32', 'tt33']:
            ChestMod.append({
                "name": "ard/"+ChestRoom1+".ard",
                "multi": [
                    {"name": "ard/jp/"+ChestRoom1+".ard"},
                    {"name": "ard/us/"+ChestRoom1+".ard"},
                    {"name": "ard/fr/"+ChestRoom1+".ard"},
                    {"name": "ard/gr/"+ChestRoom1+".ard"},
                    {"name": "ard/it/"+ChestRoom1+".ard"},
                    {"name": "ard/sp/"+ChestRoom1+".ard"},
                ],
                "method": "binarc",
                "source": [
                    {
                        "name": "m_70",
                        "type": "areadataspawn",
                        "method": "spawnpoint",
                        "source": [{"name": "chest/ard/"+ChestRoom1+"/m_70.yml"}]
                    }
                ],
            })

        for ChestRoom2 in ['bb12', 'hb05', 'hb06', 'hb26', 'tt09', 'tt10', 'tt15', 'tt16', 'tt17', 'tt22']:
            
            ChestMod.append({
                "name": "ard/"+ChestRoom2+".ard",
                "multi": [
                    {"name": "ard/jp/"+ChestRoom2+".ard"},
                    {"name": "ard/us/"+ChestRoom2+".ard"},
                    {"name": "ard/fr/"+ChestRoom2+".ard"},
                    {"name": "ard/gr/"+ChestRoom2+".ard"},
                    {"name": "ard/it/"+ChestRoom2+".ard"},
                    {"name": "ard/sp/"+ChestRoom2+".ard"},
                ],
                "method": "binarc",
                "source": [
                    {
                        "name": "m_70",
                        "type": "areadataspawn",
                        "method": "spawnpoint",
                        "source": [{"name": "chest/ard/"+ChestRoom2+"/m_70.yml"}]
                    },
                    {
                        "name": "m_71",
                        "type": "areadataspawn",
                        "method": "spawnpoint",
                        "source": [{"name": "chest/ard/"+ChestRoom2+"/m_71.yml"}]
                    }
                ],
            })

        for ChestRoom3 in ['tt07', 'tt13', 'tt14', 'tt25', 'tt26', 'tt27', 'tt28', 'tt36', 'tt37']:
            
            ChestMod.append({
                "name": "ard/"+ChestRoom3+".ard",
                "multi": [
                    {"name": "ard/jp/"+ChestRoom3+".ard"},
                    {"name": "ard/us/"+ChestRoom3+".ard"},
                    {"name": "ard/fr/"+ChestRoom3+".ard"},
                    {"name": "ard/gr/"+ChestRoom3+".ard"},
                    {"name": "ard/it/"+ChestRoom3+".ard"},
                    {"name": "ard/sp/"+ChestRoom3+".ard"},
                ],
                "method": "binarc",
                "source": [
                    {
                        "name": "m_71",
                        "type": "areadataspawn",
                        "method": "spawnpoint",
                        "source": [{"name": "chest/ard/"+ChestRoom3+"/m_71.yml"}]
                    }
                ],
            })

        #chest mdlx
        ChestMod.append({
            "name": "obj/F_EX030_SR_MSC.mdlx",
            "multi": [
                    {"name": "obj/F_EX030_SR_ABL.mdlx"},
                    {"name": "obj/F_EX030_SR_FRM.mdlx"},
                    {"name": "obj/F_EX030_SR_MAG.mdlx"},
                    {"name": "obj/F_EX030_SR_PAG.mdlx"},
                    {"name": "obj/F_EX030_SR_PRF.mdlx"},
                    {"name": "obj/F_EX030_SR_REP.mdlx"},
                    {"name": "obj/F_EX030_SR_SMN.mdlx"},
                    {"name": "obj/F_EX030_SR_VST.mdlx"},
                    {"name": "obj/F_EX030_TT_MSC.mdlx"},
                    {"name": "obj/F_EX030_TT_ABL.mdlx"},
                    {"name": "obj/F_EX030_TT_FRM.mdlx"},
                    {"name": "obj/F_EX030_TT_MAG.mdlx"},
                    {"name": "obj/F_EX030_TT_PAG.mdlx"},
                    {"name": "obj/F_EX030_TT_PRF.mdlx"},
                    {"name": "obj/F_EX030_TT_REP.mdlx"},
                    {"name": "obj/F_EX030_TT_SMN.mdlx"},
                    {"name": "obj/F_EX030_TT_VST.mdlx"},
                ],
            "method": "copy",
            "source": [
                    {
                        "name": "obj/F_EX030.mdlx",
                        "type": "internal",
                    }
                ],
        })
        ChestMod.append({
            "name": "obj/F_EX050_LK_MSC.mdlx",
            "multi": [
                    {"name": "obj/F_EX050_LK_ABL.mdlx"},
                    {"name": "obj/F_EX050_LK_FRM.mdlx"},
                    {"name": "obj/F_EX050_LK_MAG.mdlx"},
                    {"name": "obj/F_EX050_LK_PAG.mdlx"},
                    {"name": "obj/F_EX050_LK_PRF.mdlx"},
                    {"name": "obj/F_EX050_LK_REP.mdlx"},
                    {"name": "obj/F_EX050_LK_SMN.mdlx"},
                    {"name": "obj/F_EX050_LK_VST.mdlx"},
                ],
            "method": "copy",
            "source": [
                    {
                        "name": "obj/F_EX030.mdlx",
                        "type": "internal",
                    }
                ],
        })

        #chest *.a.us
        ChestMod.append({
            "name": "obj/F_EX030_SR_MSC.a.us",
            "multi": [
                    {"name": "obj/F_EX030_SR_ABL.a.us"},
                    {"name": "obj/F_EX030_SR_FRM.a.us"},
                    {"name": "obj/F_EX030_SR_MAG.a.us"},
                    {"name": "obj/F_EX030_SR_PAG.a.us"},
                    {"name": "obj/F_EX030_SR_PRF.a.us"},
                    {"name": "obj/F_EX030_SR_REP.a.us"},
                    {"name": "obj/F_EX030_SR_SMN.a.us"},
                    {"name": "obj/F_EX030_SR_VST.a.us"},
                    {"name": "obj/F_EX030_TT_MSC.a.us"},
                    {"name": "obj/F_EX030_TT_ABL.a.us"},
                    {"name": "obj/F_EX030_TT_FRM.a.us"},
                    {"name": "obj/F_EX030_TT_MAG.a.us"},
                    {"name": "obj/F_EX030_TT_PAG.a.us"},
                    {"name": "obj/F_EX030_TT_PRF.a.us"},
                    {"name": "obj/F_EX030_TT_REP.a.us"},
                    {"name": "obj/F_EX030_TT_SMN.a.us"},
                    {"name": "obj/F_EX030_TT_VST.a.us"},
                ],
            "method": "copy",
            "source": [
                    {
                        "name": "obj/F_EX030.a.us",
                        "type": "internal",
                    }
                ],
        })
        ChestMod.append({
            "name": "obj/F_EX050_LK_MSC.a.us",
            "multi": [
                    {"name": "obj/F_EX050_LK_ABL.a.us"},
                    {"name": "obj/F_EX050_LK_FRM.a.us"},
                    {"name": "obj/F_EX050_LK_MAG.a.us"},
                    {"name": "obj/F_EX050_LK_PAG.a.us"},
                    {"name": "obj/F_EX050_LK_PRF.a.us"},
                    {"name": "obj/F_EX050_LK_REP.a.us"},
                    {"name": "obj/F_EX050_LK_SMN.a.us"},
                    {"name": "obj/F_EX050_LK_VST.a.us"},
                ],
            "method": "copy",
            "source": [
                    {
                        "name": "obj/F_EX030.a.us",
                        "type": "internal",
                    }
                ],
        })
        #mset (LK)
        ChestMod.append({
            "name": "obj/F_EX030_LK.mset",
            "method": "copy",
            "source": [
                    {
                        "name": "chest/F_EX030_LK.mset",
                    }
                ],
        })

        #chest remasterd textures
        #other
        ChestMod.append({
            "name": "remastered/obj/F_EX030_SR_MSC.mdlx/-0.dds",
            "multi": [
                {"name": "remastered/obj/F_EX030_TT_MSC.mdlx/-0.dds"},
                {"name": "remastered/obj/F_EX050_LK_MSC.mdlx/-0.dds"},
            ],
            "method": "copy",
            "source": [
                {
                    "name": "chest/remastered/other.dds",
                }
            ],
        })
        #abilities
        ChestMod.append({
            "name": "remastered/obj/F_EX030_SR_ABL.mdlx/-0.dds",
            "multi": [
                {"name": "remastered/obj/F_EX030_TT_ABL.mdlx/-0.dds"},
                {"name": "remastered/obj/F_EX050_LK_ABL.mdlx/-0.dds"},
            ],
            "method": "copy",
            "source": [
                {
                    "name": "chest/remastered/abilities.dds",
                }
            ],
        })
        #forms
        ChestMod.append({
            "name": "remastered/obj/F_EX030_SR_FRM.mdlx/-0.dds",
            "multi": [
                {"name": "remastered/obj/F_EX030_TT_FRM.mdlx/-0.dds"},
                {"name": "remastered/obj/F_EX050_LK_FRM.mdlx/-0.dds"},
            ],
            "method": "copy",
            "source": [
                {
                    "name": "chest/remastered/forms.dds",
                }
            ],
        })
        #magic
        ChestMod.append({
            "name": "remastered/obj/F_EX030_SR_MAG.mdlx/-0.dds",
            "multi": [
                {"name": "remastered/obj/F_EX030_TT_MAG.mdlx/-0.dds"},
                {"name": "remastered/obj/F_EX050_LK_MAG.mdlx/-0.dds"},
            ],
            "method": "copy",
            "source": [
                {
                    "name": "chest/remastered/magic.dds",
                }
            ],
        })
        #pages
        ChestMod.append({
            "name": "remastered/obj/F_EX030_SR_PAG.mdlx/-0.dds",
            "multi": [
                {"name": "remastered/obj/F_EX030_TT_PAG.mdlx/-0.dds"},
                {"name": "remastered/obj/F_EX050_LK_PAG.mdlx/-0.dds"},
            ],
            "method": "copy",
            "source": [
                {
                    "name": "chest/remastered/pages.dds",
                }
            ],
        })
        #proofs
        ChestMod.append({
            "name": "remastered/obj/F_EX030_SR_PRF.mdlx/-0.dds",
            "multi": [
                {"name": "remastered/obj/F_EX030_TT_PRF.mdlx/-0.dds"},
                {"name": "remastered/obj/F_EX050_LK_PRF.mdlx/-0.dds"},
            ],
            "method": "copy",
            "source": [
                {
                    "name": "chest/remastered/proofs.dds",
                }
            ],
        })
        #reports
        ChestMod.append({
            "name": "remastered/obj/F_EX030_SR_REP.mdlx/-0.dds",
            "multi": [
                {"name": "remastered/obj/F_EX030_TT_REP.mdlx/-0.dds"},
                {"name": "remastered/obj/F_EX050_LK_REP.mdlx/-0.dds"},
            ],
            "method": "copy",
            "source": [
                {
                    "name": "chest/remastered/reports.dds",
                }
            ],
        })
        #summons
        ChestMod.append({
            "name": "remastered/obj/F_EX030_SR_SMN.mdlx/-0.dds",
            "multi": [
                {"name": "remastered/obj/F_EX030_TT_SMN.mdlx/-0.dds"},
                {"name": "remastered/obj/F_EX050_LK_SMN.mdlx/-0.dds"},
            ],
            "method": "copy",
            "source": [
                {
                    "name": "chest/remastered/summons.dds",
                }
            ],
        })
        #unlocks
        ChestMod.append({
            "name": "remastered/obj/F_EX030_SR_VST.mdlx/-0.dds",
            "multi": [
                {"name": "remastered/obj/F_EX030_TT_VST.mdlx/-0.dds"},
                {"name": "remastered/obj/F_EX050_LK_VST.mdlx/-0.dds"},
            ],
            "method": "copy",
            "source": [
                {
                    "name": "chest/remastered/unlocks.dds",
                }
            ],
        })

        #chest 00objentry edits
        ChestMod.append({
            "name": "00objentry.bin",
            "method": "listpatch",
            "type": "List",
            "source": [
                    {
                        "name": "chest/ChestObjList.yml",
                        "type": "objentry",
                    }
                ],
        })

        return ChestMod