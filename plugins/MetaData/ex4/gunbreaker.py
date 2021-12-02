from ..base import ActionBase, StatusBase, physic, magic


class Actions:

    class KeenEdge(ActionBase):
        """
        Delivers an attack with a potency of 200.
        1145, Keen Edge, Keen Edge, Sustaining damage over time in exchange for dealing increased damage to targets.
        """
        id = 16137
        name = {"Keen Edge", "利刃斩"}

    class NoMercy(ActionBase):
        """
        Increases damage dealt by 20%. Duration: 20s
        1831, No Mercy, No Mercy, Damage dealt is increased.
        """
        id = 16138
        name = {"No Mercy", "无情"}

    class BrutalShell(ActionBase):
        """
        Delivers an attack with a potency of 100. Combo Action: Keen Edge Combo Potency: 300 Combo Bonus: Restores own HP Cure Potency: 200(source.job==37?(source.level>=52? Combo Bonus: Creates a barrier which nullifies damage equaling HP restored Duration: 30s:):)
        1898, Brutal Shell, Brutal Shell, A highly effective defensive maneuver is nullifying damage.
        1997, Brutal Shell, Brutal Shell, A highly effective defensive maneuver is nullifying damage.
        """
        id = 16139
        name = {"Brutal Shell", "残暴弹"}
        combo_action = 16137

    class Camouflage(ActionBase):
        """
        Increases parry rate by 50% while reducing damage taken by 10%. Duration: 20s
        1832, Camouflage, Camouflage, Parry rate is increased while damage taken is reduced.
        """
        id = 16140
        name = {"Camouflage", "伪装"}

    class DemonSlice(ActionBase):
        """
        Delivers an attack with a potency of 150 to all nearby enemies.
        """
        id = 16141
        name = {"Demon Slice", "恶魔切"}

    class RoyalGuard(ActionBase):
        """
        Significantly increases enmity generation. Effect ends upon reuse.
        392, Royal Guard, Royal Guard, Enmity is increased.
        1833, Royal Guard, Royal Guard, Enmity is increased.
        """
        id = 16142
        name = {"Royal Guard", "王室亲卫"}

    class LightningShot(ActionBase):
        """
        Delivers a ranged attack with a potency of 150. Additional Effect: Increased enmity
        2392, Lightning Shot, Lightning Shot, Next weaponskill will deal increased damage.
        """
        id = 16143
        name = {"Lightning Shot", "闪雷弹"}

    class DangerZone(ActionBase):
        """
        Delivers an attack with a potency of 350.
        """
        id = 16144
        name = {"Danger Zone", "危险领域"}

    class SolidBarrel(ActionBase):
        """
        Delivers an attack with a potency of 100. Combo Action: Brutal Shell Combo Potency: 400(source.job==37?(source.level>=30? Combo Bonus: Adds a Cartridge to your Powder Gauge:):)
        """
        id = 16145
        name = {"Solid Barrel", "迅连斩"}
        combo_action = 16139

    class GnashingFang(ActionBase):
        """
        Delivers an attack with a potency of 450. (source.job==37?(source.level>=70?Additional Effect: Grants Ready to Rip Duration: 10s :):)Cartridge Cost: 1 This weaponskill does not share a recast timer with any other actions.
        """
        id = 16146
        name = {"Gnashing Fang", "烈牙"}

    class SavageClaw(ActionBase):
        """
        Delivers an attack with a potency of 550. Combo Action: Gnashing Fang(source.job==37?(source.level>=70? Combo Bonus: Grants Ready to Tear Duration: 10s:):)
        """
        id = 16147
        name = {"Savage Claw", "猛兽爪"}
        combo_action = 16146

    class Nebula(ActionBase):
        """
        Reduces damage taken by 30%. Duration: 15s
        1834, Nebula, Nebula, Damage taken is reduced.
        """
        id = 16148
        name = {"Nebula", "星云"}

    class DemonSlaughter(ActionBase):
        """
        Delivers an attack with a potency of 100 to all nearby enemies. Combo Action: Demon Slice Combo Potency: 250 Combo Bonus: Adds a Cartridge to your Powder Gauge
        """
        id = 16149
        name = {"Demon Slaughter", "恶魔杀"}
        combo_action = 16141

    class WickedTalon(ActionBase):
        """
        Delivers an attack with a potency of 650. Combo Action: Savage Claw(source.job==37?(source.level>=70? Combo Bonus: Grants Ready to Gouge Duration: 10s:):)
        """
        id = 16150
        name = {"Wicked Talon", "凶禽爪"}
        combo_action = 16147

    class Aurora(ActionBase):
        """
        Grants Regen to target. Cure Potency: 200 Duration: 18s
        1835, Aurora, Aurora, Regenerating HP over time.
        2065, Aurora, Aurora, Regenerating HP over time.
        """
        id = 16151
        name = {"Aurora", "极光"}

    class Superbolide(ActionBase):
        """
        Reduces HP to 1 and renders you impervious to most attacks. Duration: 8s
        1836, Superbolide, Superbolide, Impervious to most attacks.
        """
        id = 16152
        name = {"Superbolide", "超火流星"}

    class SonicBreak(ActionBase):
        """
        Delivers an attack with a potency of 300. Additional Effect: Damage over time Potency: 90 Duration: 30s This weaponskill does not share a recast timer with any other actions.
        1837, Sonic Break, Sonic Break, Sustaining damage over time.
        """
        id = 16153
        name = {"Sonic Break", "音速破"}

    class RoughDivide(ActionBase):
        """
        Delivers a jumping attack with a potency of 200. Maximum Charges: 2 Cannot be executed while bound.
        """
        id = 16154
        name = {"Rough Divide", "粗分斩"}

    class Continuation(ActionBase):
        """
        Allows the firing of successive rounds with your gunblade. Gnashing Fang may be followed by Jugular Rip. Savage Claw may be followed by Abdomen Tear. Wicked Talon may be followed by Eye Gouge.
        """
        id = 16155
        name = {"Continuation", "续剑"}

    class JugularRip(ActionBase):
        """
        Delivers an attack with a potency of 260. Can only be executed when Ready to Rip. ※This action cannot be assigned to a hotbar.
        """
        id = 16156
        name = {"Jugular Rip", "撕喉"}

    class AbdomenTear(ActionBase):
        """
        Delivers an attack with a potency of 280. Can only be executed when Ready to Tear. ※This action cannot be assigned to a hotbar.
        """
        id = 16157
        name = {"Abdomen Tear", "裂膛"}

    class EyeGouge(ActionBase):
        """
        Delivers an attack with a potency of 300. Can only be executed when Ready to Gouge. ※This action cannot be assigned to a hotbar.
        """
        id = 16158
        name = {"Eye Gouge", "穿目"}

    class BowShock(ActionBase):
        """
        Delivers an attack with a potency of 200 to all nearby enemies. Additional Effect: Damage over time Potency: 90 Duration: 15s
        1838, Bow Shock, Bow Shock, Sustaining damage over time.
        """
        id = 16159
        name = {"Bow Shock", "弓形冲波"}

    class HeartOfLight(ActionBase):
        """
        Reduces magic damage taken by self and nearby party members by 10%. Duration: 15s
        1839, Heart of Light, Heart of Light, Magic damage taken is reduced.
        2000, Heart of Light, Heart of Light, Damage taken is reduced.
        """
        id = 16160
        name = {"Heart of Light", "光之心"}

    class HeartOfStone(ActionBase):
        """
        Reduces damage taken by a party member or self by 15%. Duration: 7s Additional Effect: When targeting a party member while under the effect of Brutal Shell, that effect is also granted to the target Duration: 30s
        1840, Heart of Stone, Heart of Stone, Damage taken is reduced.
        """
        id = 16161
        name = {"Heart of Stone", "石之心"}

    class BurstStrike(ActionBase):
        """
        Delivers an attack with a potency of 500. Cartridge Cost: 1
        """
        id = 16162
        name = {"Burst Strike", "爆发击"}

    class FatedCircle(ActionBase):
        """
        Delivers an attack with a potency of 320 to all nearby enemies. Cartridge Cost: 1
        """
        id = 16163
        name = {"Fated Circle", "命运之环"}

    class Bloodfest(ActionBase):
        """
        Draws aetheric energy from target, adding 2 Cartridges to your Powder Gauge.
        """
        id = 16164
        name = {"Bloodfest", "血壤"}

    class BlastingZone(ActionBase):
        """
        Delivers an attack with a potency of 800.
        """
        id = 16165
        name = {"Blasting Zone", "爆破领域"}
