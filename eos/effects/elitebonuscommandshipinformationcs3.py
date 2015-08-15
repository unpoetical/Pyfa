# eliteBonusCommandShipInformationCS3
#
# Used by:
# Ships from group: Command Ship (4 of 8)
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Information Warfare Specialist"),
                                  "commandBonus", module.getModifiedItemAttr("eliteBonusCommandShips3"), skill="Command Ships")
