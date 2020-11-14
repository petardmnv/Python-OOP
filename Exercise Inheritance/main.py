from players_and_monster.hero import Hero
from players_and_monster.elf import Elf
from players_and_monster.wizard import Wizard
from players_and_monster.muse_elf import MuseElf
from players_and_monster.knight import Knight
from players_and_monster.blade_knight import BladeKnight
from players_and_monster.dark_knight import DarkKnight
from players_and_monster.dark_wizard import DarkWizard
from players_and_monster.soul_master import SoulMaster


hero = Hero("H", 3)

print(hero.username)

print(hero.level)

print(str(hero))

elf = Elf("E", 4)

print(str(elf))

m_e = MuseElf("ME", 14)

print(str(m_e))

w = Wizard("W", 2)

print(str(w))

d_w = DarkWizard("DW", 12)

print(str(d_w))

s_w = SoulMaster("SW", 22)

print(str(s_w))

k = Knight("K", 7)

print(str(k))

d_k = DarkKnight("DK", 17)

print(str(d_k))

b_k = BladeKnight("BK", 27)

print(str(b_k))