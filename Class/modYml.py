class modYml:
    retryDarkThorn = "retryDarkThorn"
    retryDataXemnas = "retryDataXemnas"

    def getDefaultMod():
        return {
            "title": "Randomizer Seed",
            "assets": [
                {
                    "name": "msg/us/sys.bar",
                    "multi": [
                        {"name": "msg/fr/sys.bar"},
                        {"name": "msg/gr/sys.bar"},
                        {"name": "msg/it/sys.bar"},
                        {"name": "msg/sp/sys.bar"},
                    ],
                    "method": "binarc",
                    "source": [
                        {
                            "name": "sys",
                            "type": "list",
                            "method": "kh2msg",
                            "source": [
                                {
                                    "name": "sys.yml",
                                    "language": "en"
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": "msg/jp/sys.bar",
                    "platform": "ps2",
                    "method": "binarc",
                    "source": [
                        {
                            "name": "sys",
                            "type": "list",
                            "method": "kh2msg",
                            "source": [
                                {
                                    "name": "sys.yml",
                                    "language": "en"
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": "msg/jp/sys.bar",
                    "platform": "pc",
                    "method": "binarc",
                    "source": [
                        {
                            "name": "sys",
                            "type": "list",
                            "method": "kh2msg",
                            "source": [
                                {
                                    "name": "sys.yml",
                                    "language": "jp"
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": "00battle.bin",
                    "method": "binarc",
                    "source": [
                        {
                            "name": "fmlv",
                            "method": "listpatch",
                            "type": "List",
                            "source": [
                                {
                                    "name": "FmlvList.yml",
                                    "type": "fmlv"
                                }
                            ]
                        },
                        {
                            "name": "lvup",
                            "method": "listpatch",
                            "type": "List",
                            "source": [
                                {
                                    "name": "LvupList.yml",
                                    "type": "lvup"
                                }
                            ]
                        },
                        {
                            "name": "bons",
                            "method": "listpatch",
                            "type": "List",
                            "source": [
                                {
                                    "name": "BonsList.yml",
                                    "type": "bons"
                                }
                            ]
                        },
                        {
                            "name": "plrp",
                            "method": "listpatch",
                            "type": "List",
                            "source": [
                                {
                                    "name": "PlrpList.yml",
                                    "type": "plrp"
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": "03system.bin",
                    "method": "binarc",
                    "source": [
                        {
                            "name": "trsr",
                            "method": "listpatch",
                            "type": "List",
                            "source": [
                                {
                                    "name": "TrsrList.yml",
                                    "type": "trsr"
                                }
                            ]
                        },
                        {
                            "name": "item",
                            "method": "listpatch",
                            "type": "List",
                            "source": [
                                {
                                    "name": "ItemList.yml",
                                    "type": "item"
                                }
                            ]
                        }
                    ]
                }
            ]
        }

    def getSysYAML(seedHashIcons, crit_mode = False, final_door = 'ALLPROOF'):
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
        if final_door == 'OBJECTIVES':
            sys.append({"id": 15115, "en": "Completion Mark"})
            sys.append({"id": 15116, "en": "An Objective Completion Mark.\nAwarded to those who complete given tasks.\n7 of these are required to open the door..."})
        return sys
    
    def getJmYAML(objectives):
        jm = []

        #reportId = 14051
        #counter = 1
        #for task in objectives:
        #    if reportId == 14071:
        #        reportId = 14254
        #    jm.append({"id": reportId, "en": "Objective "+str(counter)})
        #    jm.append({"id": reportId+1, "en": task.Name})
        #    reportId+=2
        #    counter+=1
        #redo. gonna have all lines in a single report entry (unused report 14)

        jm.append({"id": 13945, "en": "Objectives"})
        jm.append({"id": 14260, "en": "Objective List"})
        listText = ''
        counter = 1
        for task in objectives:
            listText += str(counter)+'. '+task.Name+'\n'
            counter+=1
        jm.append({"id": 14261, "en": listText})

        return jm

    def getObjectiveMsgMod():
        ObjectiveMod = []

        ObjectiveMod.append({
            "name": "msg/us/jm.bar",
            "multi": [
                {"name": "msg/fr/jm.bar"},
                {"name": "msg/gr/jm.bar"},
                {"name": "msg/it/jm.bar"},
                {"name": "msg/sp/jm.bar"},
            ],
            "method": "binarc",
            "source": [
                {
                    "name": "jm",
                    "type": "list",
                    "method": "kh2msg",
                    "source": [
                        {
                            "name": "jm.yml",
                            "language": "en"
                        }
                    ]
                }
            ]
        })

        ObjectiveMod.append({
            "name": "remastered/itempic/item-226.imd/-0.dds",
            "method": "copy",
            "platform": "pc",
            "source": [
                {
                    "name": "objectives/remastered/completionmark.dds",
                }
            ]
        })

        return ObjectiveMod

    def getObjectiveBarMod(pc = False, puzz = False):
        if not puzz:
            mod_dict = {
                        "method": "binarc",
                        "source": [
                            {
                                "name": "anse",
                                "type": "jimidata",
                                "method": "copy",
                                "source": [
                                    {
                                        "name": "objectives/ansem.bin"
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
        else:
            mod_dict = [{
                        "name": "anse",
                        "type": "jimidata",
                        "method": "copy",
                        "source": [
                            {
                                "name": "objectives/ansem.bin"
                            }
                        ]
                    }]
            return mod_dict

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

