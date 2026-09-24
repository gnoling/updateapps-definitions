# updateapps definitions

Definitions for [updateapps](https://github.com/gnoling/updateapps): one YAML file per app in
`apps.d/`, named `<id>.yaml`.

## Use it

updateapps uses this repository by default, opt-in. `updateapps list` shows what's here;
name what you want in `~/.config/updateapps/config.yaml`:

```yaml
enabled: [dolphin, rpcs3]
```

Nothing here needs `trusted: true`: no definition runs shell commands, installs as root, or
writes outside your apps directories.

## Definitions

130 definitions. *(disabled)* marks ones that stay off even for a repository that enables
everything by default (upstream archived or moved); their `notes:` say why.

### Emulators

| Definition | Description | Upstream |
|---|---|---|
| [ares](apps.d/ares.yaml) | Multi-system retro console emulator | [bmsuseluda/ares-emu-appimage](https://github.com/bmsuseluda/ares-emu-appimage) |
| [Azahar](apps.d/azahar.yaml) | An open-source 3DS emulator project based on Citra | [azahar-emu/azahar](https://github.com/azahar-emu/azahar) |
| [Basilisk II](apps.d/basiliskii.yaml) | 68k Macintosh emulator for running classic Mac OS (7.x - 8.1) | [Korkman/macemu-appimage-builder](https://github.com/Korkman/macemu-appimage-builder) |
| [BigInstinct](apps.d/biginstinct.yaml) | Killer Instinct arcade emulator by Rich Whitehouse | [www.richwhitehouse.com](https://www.richwhitehouse.com/ki/index.php?content=download) |
| [BigPEmu](apps.d/bigpemu.yaml) | Atari Jaguar and Jaguar CD emulator | [www.richwhitehouse.com](https://www.richwhitehouse.com/jaguar/index.php?content=download) |
| [BizHawk](apps.d/bizhawk.yaml) | Multi-system emulator focused on TAS (tool-assisted speedrun) creation | [TASEmulators/BizHawk](https://github.com/TASEmulators/BizHawk) |
| [BlastEm](apps.d/blastem.yaml) | High-accuracy Sega Genesis / Mega Drive emulator | [www.retrodev.com](https://www.retrodev.com/blastem/nightlies/) |
| [Cemu](apps.d/cemu.yaml) | Nintendo Wii U Emulator | [cemu-project/Cemu](https://github.com/cemu-project/Cemu) |
| [Chiaki-NG](apps.d/chiaki-ng.yaml) | PS4/PS5 Remote Play streaming client | [streetpea/chiaki-ng](https://github.com/streetpea/chiaki-ng) |
| [Citron](apps.d/citron.yaml) | Nintendo Switch emulator | [citron-neo/CI](https://github.com/citron-neo/CI) |
| [ClownMDEmu](apps.d/clownmdemu.yaml) | Sega Genesis/Mega Drive Emulator | [Clownacy/clownmdemu-frontend](https://github.com/Clownacy/clownmdemu-frontend) |
| [Delta Patcher](apps.d/deltapatcher.yaml) | Create and apply xdelta binary patches | [marco-calautti/DeltaPatcher](https://github.com/marco-calautti/DeltaPatcher) |
| [Dolphin](apps.d/dolphin.yaml) | Nintendo GameCube and Wii emulator | [qurious-pixel/dolphin](https://github.com/qurious-pixel/dolphin) |
| [DuckStation](apps.d/duckstation.yaml) | Fast PlayStation 1 emulator | [stenzek/duckstation](https://github.com/stenzek/duckstation) |
| [Eden](apps.d/eden.yaml) | Nintendo Switch emulator (continuation of the Yuzu project) | Lua, [git.eden-emu.dev](https://git.eden-emu.dev/api/v1/repos/eden-ci/nightly/releases?limit=1) |
| [EKA2L1](apps.d/eka2l1.yaml) | Symbian OS / Nokia N-Gage emulator | [EKA2L1/EKA2L1](https://github.com/EKA2L1/EKA2L1) |
| [FinalBurn Neo](apps.d/fbneo.yaml) | Multi-system arcade emulator (Neo Geo, CPS1/2/3, and many arcade boards) | [finalburnneo/FBNeo](https://github.com/finalburnneo/FBNeo) |
| [Flycast Dojo](apps.d/flycast-dojo.yaml) | Sega Dreamcast emulator with rollback netplay support | [blueminder/flycast-dojo](https://github.com/blueminder/flycast-dojo) |
| [Flycast](apps.d/flycast.yaml) | Sega Dreamcast/Naomi/Atomiswave emulator | Lua, [flycast-builds.s3.fr-par.scw.cloud](https://flycast-builds.s3.fr-par.scw.cloud/) |
| [FS-UAE](apps.d/fs-uae.yaml) | Commodore Amiga emulator (UAE-based, all Amiga models) | [FrodeSolheim/fs-uae](https://github.com/FrodeSolheim/fs-uae) |
| [Fujisan](apps.d/fujisan.yaml) | Atari 8-bit computer emulator with built-in FujiNet support | [pedgarcia/fujisan](https://github.com/pedgarcia/fujisan) |
| [Gearboy](apps.d/gearboy.yaml) | Nintendo Game Boy and Game Boy Color emulator | [drhelius/Gearboy](https://github.com/drhelius/Gearboy) |
| [Gearcoleco](apps.d/gearcoleco.yaml) | ColecoVision emulator | [drhelius/Gearcoleco](https://github.com/drhelius/Gearcoleco) |
| [Geargrafx](apps.d/geargrafx.yaml) | NEC PC Engine / TurboGrafx-16 / SuperGrafx emulator | [drhelius/Geargrafx](https://github.com/drhelius/Geargrafx) |
| [Gearlynx](apps.d/gearlynx.yaml) | Atari Lynx emulator | [drhelius/Gearlynx](https://github.com/drhelius/Gearlynx) |
| [Gearsystem](apps.d/gearsystem.yaml) | Sega Master System, Game Gear, and SG-1000 emulator | [drhelius/Gearsystem](https://github.com/drhelius/Gearsystem) |
| [gopher64](apps.d/gopher64.yaml) | Nintendo 64 emulator written in Rust | [gopher64/gopher64](https://github.com/gopher64/gopher64) |
| [Hades](apps.d/hades.yaml) | Highly accurate Game Boy Advance emulator | [hades-emu/Hades](https://github.com/hades-emu/Hades) |
| [Hypseus Singe](apps.d/hypseus.yaml) | Multiple Arcade Laserdisc Emulator (Dragon's Lair, Space Ace, Singe games) | [DirtBagXon/hypseus-singe](https://github.com/DirtBagXon/hypseus-singe) |
| [jgenesis](apps.d/jgenesis.yaml) | Multi-system emulator for Sega Genesis, Master System, SNES, NES, Game Boy and more | [jsgroth/jgenesis](https://github.com/jsgroth/jgenesis) |
| [Lime3DS](apps.d/lime3ds.yaml) *(disabled)* | Nintendo 3DS emulator (Citra fork) | [Lime3DS/lime3ds-archive](https://github.com/Lime3DS/lime3ds-archive) |
| [Mandarine](apps.d/mandarine3ds.yaml) | Nintendo 3DS emulator (fork of Citra) | [mandarine3ds/mandarine](https://github.com/mandarine3ds/mandarine) |
| [melonDS](apps.d/melonds.yaml) | A fast and accurate Nintendo DS emulator | [melonDS-emu/melonDS](https://github.com/melonDS-emu/melonDS) |
| [Mesen](apps.d/mesen.yaml) *(disabled)* | High-accuracy NES/Famicom and SNES emulator | [SourMesen/Mesen2](https://github.com/SourMesen/Mesen2) |
| [mGBA](apps.d/mgba.yaml) | Game Boy Advance Emulator | [s3.amazonaws.com](https://s3.amazonaws.com/mgba/mGBA-build-latest-appimage-x64.appimage) |
| [NanoBoyAdvance](apps.d/nanoboyadvance.yaml) *(disabled)* | Cycle-accurate Game Boy Advance emulator | [nba-emu/NanoBoyAdvance](https://github.com/nba-emu/NanoBoyAdvance) |
| [Obentou](apps.d/obentou.yaml) | NEC PC Engine / TurboGrafx-16 emulator | [yughias/Obentou](https://github.com/yughias/Obentou) |
| [PCSX2](apps.d/pcsx2.yaml) | Sony PlayStation 2 Emulator | [PCSX2/pcsx2](https://github.com/PCSX2/pcsx2) |
| [PPSSPP](apps.d/ppsspp.yaml) | Sony PlayStation Portable (PSP) Emulator | [hrydgard/ppsspp](https://github.com/hrydgard/ppsspp) |
| [puNES](apps.d/punes.yaml) | Nintendo Entertainment System Emulator | [punesemu/puNES](https://github.com/punesemu/puNES) |
| [RMG](apps.d/rmg.yaml) | Rosalie's Mupen GUI - Nintendo 64 emulator frontend | [Rosalie241/RMG](https://github.com/Rosalie241/RMG) |
| [RPCS3](apps.d/rpcs3.yaml) | Sony PlayStation 3 Emulator | [RPCS3/rpcs3-binaries-linux](https://github.com/RPCS3/rpcs3-binaries-linux) |
| [Ryujinx (stable)](apps.d/ryujinx-stable-releases.yaml) *(disabled)* | Nintendo Switch emulator | [Ryubing/Stable-Releases](https://github.com/Ryubing/Stable-Releases) |
| [Ryujinx](apps.d/ryujinx.yaml) *(disabled)* | Nintendo Switch emulator | [Ryubing/Ryujinx](https://github.com/Ryubing/Ryujinx) |
| [shadPS4 Qt Launcher](apps.d/shadps4qtlauncher.yaml) | Qt launcher for the shadPS4 PlayStation 4 emulator | [shadps4-emu/shadps4-qtlauncher](https://github.com/shadps4-emu/shadps4-qtlauncher) |
| [shadPS4](apps.d/shadps4.yaml) | Sony PlayStation 4 emulator | [shadps4-emu/shadPS4](https://github.com/shadps4-emu/shadPS4) |
| [SheepShaver](apps.d/sheepshaver.yaml) | PowerPC Macintosh emulator for running classic Mac OS | [Korkman/macemu-appimage-builder](https://github.com/Korkman/macemu-appimage-builder) |
| [SkyEmu](apps.d/skyemu.yaml) | Game Boy, Game Boy Advance, and Nintendo DS emulator | [skylersaleh/SkyEmu](https://github.com/skylersaleh/SkyEmu) |
| [Snes9x](apps.d/snes9x.yaml) *(disabled)* | Super Nintendo Entertainment System Emulator | [snes9xgit/snes9x](https://github.com/snes9xgit/snes9x) |
| [Supermodel](apps.d/supermodel.yaml) | Sega Model 3 arcade system emulator | [trzy/Supermodel](https://github.com/trzy/Supermodel) |
| [SUPERZSNES](apps.d/superzsnes.yaml) | Modern Unity-based revival of the ZSNES Super Nintendo emulator | [www.zsnes.com](https://www.zsnes.com/) |
| [Tanuki3DS](apps.d/tanuki3ds.yaml) | Nintendo 3DS Emulator | [burhanr13/Tanuki3DS](https://github.com/burhanr13/Tanuki3DS) |
| [Vita3K](apps.d/vita3k.yaml) | PlayStation Vita Emulator | [Vita3K/Vita3K](https://github.com/Vita3K/Vita3K) |
| [xemu](apps.d/xemu.yaml) | Original Microsoft Xbox game console emulator | [xemu-project/xemu](https://github.com/xemu-project/xemu) |
| [Xenia Edge](apps.d/xenia-edge.yaml) | Xbox 360 emulator for Linux | [has207/xenia-edge](https://github.com/has207/xenia-edge) |
| [Xenia](apps.d/xenia.yaml) | Xbox 360 emulator (canary/development build) | [xenia-canary/xenia-canary-releases](https://github.com/xenia-canary/xenia-canary-releases) |
| [Ymir](apps.d/ymir.yaml) | Sega Saturn emulator | [StrikerX3/Ymir](https://github.com/StrikerX3/Ymir) |

### Ports and recompilations

| Definition | Description | Upstream |
|---|---|---|
| [2 Ship 2 Harkinian](apps.d/2ship2harkinian.yaml) | Native PC port of The Legend of Zelda: Majora's Mask | [HarbourMasters/2ship2harkinian](https://github.com/HarbourMasters/2ship2harkinian) |
| [Augustus](apps.d/augustus.yaml) | Enhanced open-source re-implementation of Caesar III | [Keriew/augustus](https://github.com/Keriew/augustus) |
| [Banjo-Kazooie: Recompiled](apps.d/banjorecompiled.yaml) | PC port of Banjo-Kazooie via N64 static recompilation | [BanjoRecomp/BanjoRecomp](https://github.com/BanjoRecomp/BanjoRecomp) |
| [Bomberman 64: Recompiled](apps.d/bm64recompiled.yaml) | PC port of Bomberman 64 via N64 static recompilation | [RevoSucks/BM64Recomp](https://github.com/RevoSucks/BM64Recomp) |
| [CorsixTH (Theme Hospital)](apps.d/corsixth.yaml) | Open-source reimplementation of the Bullfrog game Theme Hospital | [CorsixTH/CorsixTH](https://github.com/CorsixTH/CorsixTH) |
| [Crash Bandicoot: Recompiled](apps.d/crashbandicoot.yaml) | PC port of Crash Bandicoot (NTSC-U, SCUS-94900) via RecompOne PS1 recompilation — needs your own .cue/.bin | [Matteo842/CrashBandicoot-Launcher](https://github.com/Matteo842/CrashBandicoot-Launcher) |
| [Dethrace](apps.d/dethrace.yaml) | Reverse-engineered Carmageddon (1997) engine — needs the original DATA folder here | [dethrace-labs/dethrace](https://github.com/dethrace-labs/dethrace) |
| [DevilutionX (Diablo)](apps.d/devilutionx.yaml) | Open-source reimplementation of Diablo 1 and Hellfire | [diasurgical/devilutionX](https://github.com/diasurgical/devilutionX) |
| [Dinosaur Planet: Recompiled](apps.d/dinosaurplanetrecompiled.yaml) | PC port of the unreleased N64 game Dinosaur Planet | [DinosaurPlanetRecomp/dino-recomp](https://github.com/DinosaurPlanetRecomp/dino-recomp) |
| [DREAMM](apps.d/dreamm.yaml) | DOS Retro-Engine Emulator for Aaron Giles' Multi-Media games (LucasArts adventure runtime) | [dreamm.aarongiles.com](https://dreamm.aarongiles.com/) |
| [DSDA-Doom](apps.d/dsda-doom.yaml) | Doom source port focused on speedrunning, demos, and accurate replays | [kraflab/dsda-doom](https://github.com/kraflab/dsda-doom) |
| [Duke Nukem: Zero Hour Recompiled](apps.d/dnzh.yaml) | PC port of Duke Nukem: Zero Hour via N64 static recompilation | [dnzh-overclocked.com](https://dnzh-overclocked.com/) |
| [Dusk (Twilight Princess)](apps.d/dusk.yaml) | Open-source PC port of The Legend of Zelda: Twilight Princess | [TwilitRealm/dusk](https://github.com/TwilitRealm/dusk) |
| [Ghost Ship](apps.d/ghostship.yaml) | Native PC port of Super Mario 64 | [HarbourMasters/Ghostship](https://github.com/HarbourMasters/Ghostship) |
| [Golden Balloon](apps.d/golden-balloon.yaml) | A native port of the 1997 Nintendo 64 kart racer, Diddy Kong Racing | [akratch/goldenballoon](https://github.com/akratch/goldenballoon) |
| [Harvest Moon 64: Recompiled](apps.d/harvestmoon64.yaml) | PC port of Harvest Moon 64 via N64 static recompilation | [HarvestMoon64Recomp/HarvestMoon64Recomp](https://github.com/HarvestMoon64Recomp/HarvestMoon64Recomp) |
| [Heroes of Might and Magic II (fheroes2)](apps.d/fheroes2.yaml) | Open-source reimplementation of Heroes of Might and Magic II | [ihhub/fheroes2](https://github.com/ihhub/fheroes2) |
| [Ironwail](apps.d/ironwail.yaml) | High-performance Quake source port for modern hardware and large maps | [andrei-drexler/ironwail](https://github.com/andrei-drexler/ironwail) |
| [Kameo: Elements of Power (RePowered)](apps.d/kameo.yaml) | PC port of the Xbox 360 game Kameo: Elements of Power (vanilla build - the TU build renders black) | [birabittoh/KameoRePowered](https://github.com/birabittoh/KameoRePowered) |
| [Kirby's Return to Dream Land: Recompiled](apps.d/kirbywiirecomp.yaml) | PC port of Kirby's Return to Dream Land via Wii recompilation (ModernGekko) | [ExpansionPak/ModernGekko](https://github.com/ExpansionPak/ModernGekko) |
| [Lighthouse (Banjo-Kazooie)](apps.d/lighthouse.yaml) | Harbour Masters native PC port of Banjo-Kazooie | [HarbourMasters/Lighthouse](https://github.com/HarbourMasters/Lighthouse) |
| [Lost Odyssey Recomp](apps.d/lostodysseyrecomp.yaml) | Experimental native PC port of Lost Odyssey using static recompilation | [freefrank/LostOdysseyRecomp](https://github.com/freefrank/LostOdysseyRecomp) |
| [Mega Man 64: Recompiled](apps.d/megaman64recompiled.yaml) | PC port of Mega Man 64 via N64 static recompilation | [MegaMan64Recomp/MegaMan64Recompiled](https://github.com/MegaMan64Recomp/MegaMan64Recompiled) |
| [Mystical Ninja Starring Goemon: Recompiled](apps.d/goemon64recompiled.yaml) | PC port of Mystical Ninja Starring Goemon via N64 static recompilation | [klorfmorf/Goemon64Recomp](https://github.com/klorfmorf/Goemon64Recomp) |
| [OpenGOAL Launcher](apps.d/open-goal-launcher.yaml) | Launcher for OpenGOAL - the Jak and Daxter PC port project | [open-goal/launcher](https://github.com/open-goal/launcher) |
| [OpenMW](apps.d/openmw.yaml) | Open-source reimplementation of The Elder Scrolls III: Morrowind | [OpenMW/openmw](https://github.com/OpenMW/openmw) |
| [OpenRA - Dune 2000](apps.d/openra-dune-2000.yaml) | Open-source remake of Dune 2000 using the OpenRA engine | [OpenRA/OpenRA](https://github.com/OpenRA/OpenRA) |
| [OpenRA - Red Alert](apps.d/openra-red-alert.yaml) | Open-source remake of Command & Conquer: Red Alert | [OpenRA/OpenRA](https://github.com/OpenRA/OpenRA) |
| [OpenRA - Tiberian Dawn](apps.d/openra-tiberian-dawn.yaml) | Open-source remake of Command & Conquer: Tiberian Dawn | [OpenRA/OpenRA](https://github.com/OpenRA/OpenRA) |
| [OpenRCT2](apps.d/openrct2.yaml) | Open-source reimplementation of RollerCoaster Tycoon 2 | [OpenRCT2/OpenRCT2](https://github.com/OpenRCT2/OpenRCT2) |
| [OpenTDU](apps.d/opentdu.yaml) | Open-source reimplementation of Test Drive Unlimited (overlay for an existing install) | [opentestdriveunlimited/OpenTestDriveUnlimited](https://github.com/opentestdriveunlimited/OpenTestDriveUnlimited) |
| [OpenTTD](apps.d/openttd.yaml) | Open-source reimplementation of Transport Tycoon Deluxe | [cdn.openttd.org](https://cdn.openttd.org/openttd-releases/latest.yaml) |
| [PaperBoat](apps.d/paperboat.yaml) | Native PC port of Paper Mario 64 | [HarbourMasters/PaperBoat](https://github.com/HarbourMasters/PaperBoat) |
| [Perfect Dark](apps.d/pd.yaml) | Modern native PC port of Perfect Dark, decompiled from the N64 original | [perfect-dark-pc-port/perfect_dark](https://github.com/perfect-dark-pc-port/perfect_dark) |
| [PsyDoom](apps.d/psydoom.yaml) | Reverse-engineered PC port of PlayStation Doom and Final Doom | [BodbDearg/PsyDoom](https://github.com/BodbDearg/PsyDoom) |
| [re:Blue](apps.d/reblue.yaml) | Native PC rebuild of Blue Dragon (Xbox 360) via static recompilation | [zolaware/reblue](https://github.com/zolaware/reblue) |
| [REDRIVER2](apps.d/redriver2.yaml) | PC port of Driver 2 reverse-engineered from the PlayStation original | [OpenDriver2/REDRIVER2](https://github.com/OpenDriver2/REDRIVER2) |
| [RuneScape Classic](apps.d/rsc-c.yaml) | RuneScape Classic client in C — self-contained, connects to community servers | [2003scape/rsc-c](https://github.com/2003scape/rsc-c) |
| [Severed Chains](apps.d/severedchains.yaml) | The Legend of Dragoon decompiled to Java — put all four PS1 discs in severedchains/isos | [Legend-of-Dragoon-Modding/Severed-Chains](https://github.com/Legend-of-Dragoon-Modding/Severed-Chains) |
| [Ship of Harkinian](apps.d/soh.yaml) | Native PC port of The Legend of Zelda: Ocarina of Time | [HarbourMasters/Shipwright](https://github.com/HarbourMasters/Shipwright) |
| [Snowboard Kids 2: Recompiled](apps.d/snowboardkids2.yaml) | PC port of Snowboard Kids 2 via N64 static recompilation | [cdlewis/snowboardkids2-recomp](https://github.com/cdlewis/snowboardkids2-recomp) |
| [Sonic 1 & 2 (RSDKv4)](apps.d/rsdkv4.yaml) | Sonic the Hedgehog 1 & 2 (2013) decompilation — needs Data.rsdk from the mobile release | [RSDKModding/RSDKv4-Decompilation](https://github.com/RSDKModding/RSDKv4-Decompilation) |
| [Sonic 3 A.I.R.](apps.d/sonic3air.yaml) | Sonic 3: Angel Island Revisited - enhanced PC port of Sonic 3 & Knuckles | [Eukaryot/sonic3air](https://github.com/Eukaryot/sonic3air) |
| [Sonic CD (RSDKv3)](apps.d/rsdkv3.yaml) | Sonic CD (2011) decompilation — needs Data.rsdk from the mobile release beside the binary | [RSDKModding/RSDKv3-Decompilation](https://github.com/RSDKModding/RSDKv3-Decompilation) |
| [Spaghetti Kart](apps.d/spaghettikart.yaml) | Native PC port of Mario Kart 64 | [HarbourMasters/SpaghettiKart](https://github.com/HarbourMasters/SpaghettiKart) |
| [Starship](apps.d/starship.yaml) | Native PC port of Star Fox 64 | [HarbourMasters/Starship](https://github.com/HarbourMasters/Starship) |
| [Super Mario 64: CoopDX](apps.d/sm64coopdx.yaml) | Online co-op multiplayer PC port of Super Mario 64 | [coop-deluxe/sm64coopdx](https://github.com/coop-deluxe/sm64coopdx) |
| [Super Mario Bros. Remastered](apps.d/smb-remastered.yaml) | Fan remaster of the original Super Mario Bros. built in Godot | [JHDev2006/Super-Mario-Bros.-Remastered-Public](https://github.com/JHDev2006/Super-Mario-Bros.-Remastered-Public) |
| [The Legend of Zelda: The Minish Cap](apps.d/minishcap.yaml) | PC port of The Legend of Zelda: The Minish Cap | [999sian/tmc](https://github.com/999sian/tmc) |
| [TRX (Tomb Raider I-III)](apps.d/trx.yaml) | Open-source reimplementation and enhancement of Tomb Raider I-III and their expansions (unified TRX engine) | [LostArtefacts/TRX](https://github.com/LostArtefacts/TRX) |
| [Unleashed Recompiled](apps.d/unleashedrecomp.yaml) | PC port of the Xbox 360 Sonic Unleashed via static recompilation | [hedge-dev/UnleashedRecomp](https://github.com/hedge-dev/UnleashedRecomp) |
| [vkQuake](apps.d/vkquake.yaml) | Vulkan-rendered Quake source port (QuakeSpasm-based) | [Novum/vkQuake](https://github.com/Novum/vkQuake) |
| [Woof!](apps.d/woof.yaml) | Vanilla-feel Doom source port with modern conveniences | [fabiangreffrath/woof](https://github.com/fabiangreffrath/woof) |
| [Zelda 64: Recompiled](apps.d/zelda64recompiled.yaml) | PC port of The Legend of Zelda: Majora's Mask via N64 recompilation | [Zelda64Recomp/Zelda64Recomp](https://github.com/Zelda64Recomp/Zelda64Recomp) |
| [Zelda: Link's Awakening DX HD](apps.d/ladxhd.yaml) | Fan-made HD remake of The Legend of Zelda: Link's Awakening DX | [bighead.0/ladxhd_updated](https://gitlab.com/bighead.0/ladxhd_updated) |

### Tools

| Definition | Description | Upstream |
|---|---|---|
| [86Box](apps.d/86box.yaml) | Emulator of classic IBM PC compatibles and DOS-era hardware | [86Box/86Box](https://github.com/86Box/86Box) |
| [Avidemux](apps.d/avidemux.yaml) | Video editor (nightly build) | [www.avidemux.org](https://www.avidemux.org/nightly/appImage/) |
| [Bforartists](apps.d/bforartists.yaml) | A fork of Blender focused on improved usability and user interface | [Bforartists/Bforartists](https://github.com/Bforartists/Bforartists) |
| [ComicTagger](apps.d/comictagger.yaml) | Comic book metadata tagging and management tool | [comictagger/comictagger](https://github.com/comictagger/comictagger) |
| [Czkawka](apps.d/czkawka-gui.yaml) | Fast duplicate file, empty folder, and similar image finder | [qarmin/czkawka](https://github.com/qarmin/czkawka) |
| [digiKam](apps.d/digikam.yaml) | Professional photo management and editing application | [files.kde.org](https://files.kde.org/digikam/) |
| [DOSBox Pure Unleashed](apps.d/dosbox-pure.yaml) | Standalone DOSBox Pure build for running DOS games and applications | [schellingb/dosbox-pure-unleashed](https://github.com/schellingb/dosbox-pure-unleashed) |
| [DOSBox Staging](apps.d/dosbox-staging.yaml) | Modern continuation of DOSBox with advanced features | [dosbox-staging/dosbox-staging](https://github.com/dosbox-staging/dosbox-staging) |
| [Heroic Games Launcher](apps.d/heroicgamelauncher.yaml) | An alternative GOG and Epic Games Launcher for Linux, Windows and macOS | [Heroic-Games-Launcher/HeroicGamesLauncher](https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher) |
| [Inkscape](apps.d/inkscape.yaml) | Professional vector graphics editor (SVG) | [inkscape.org](https://inkscape.org/release/all/gnulinux/appimage/) |
| [Joplin](apps.d/joplin.yaml) | Open-source note-taking and to-do app with sync | [laurent22/joplin](https://github.com/laurent22/joplin) |
| [Krita](apps.d/krita.yaml) | Professional free and open source digital painting program | [krita.org](https://krita.org/en/download/) |
| [LosslessCut](apps.d/losslesscut.yaml) | Lossless video and audio editor for trimming and cutting media files | [mifi/lossless-cut](https://github.com/mifi/lossless-cut) |
| [Ludusavi](apps.d/ludusavi.yaml) | Backup and restore tool for PC game save files | [mtkennerly/ludusavi](https://github.com/mtkennerly/ludusavi) |
| [Obsidian](apps.d/obsidian.yaml) | Markdown-based knowledge base / note-taking app | [obsidianmd/obsidian-releases](https://github.com/obsidianmd/obsidian-releases) |
| [ProtonUp-Qt](apps.d/protonup-qt.yaml) | Install and manage Proton-GE and other Wine/Proton compatibility layers | [DavidoTek/ProtonUp-Qt](https://github.com/DavidoTek/ProtonUp-Qt) |
| [spotifyd](apps.d/spotifyd.yaml) | Spotify Connect daemon | [Spotifyd/spotifyd](https://github.com/Spotifyd/spotifyd) |
| [WinBoat](apps.d/winboat.yaml) | Windows application compatibility and launcher tool | [TibixDev/winboat](https://github.com/TibixDev/winboat) |

## Contribute

Add or edit one file in `apps.d/` and open a pull request. There's nothing to build or
package: updateapps downloads the branch as the archive the host generates on request.

- Check it first: `updateapps --defs apps.d validate`, then `updateapps --defs apps.d check <id>`.
- Prefer a declarative `source:`; reach for Lua only when upstream's publishing can't be
  described otherwise (see updateapps' `docs/DEFINITIONS.md` and `docs/LUA.md`).
- `name:` is the app's proper name, `description:` one sentence-case line.
- Use `${APPDIR}` / `${APPIMAGEDIR}`, never a literal home directory.
- Put anything a maintainer should know (why a pattern is odd, what upstream changed) in `notes:`.
- Run `tools/readme-table.py` to refresh the table above (needs Python with PyYAML).

## License

[CC0](LICENSE): public domain. Copy definitions into your own repository freely; no
attribution needed.
