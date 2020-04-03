# coding=utf-8
from honeybee_energy.constructionset import ConstructionSet
from honeybee_energy.construction.opaque import OpaqueConstruction
from honeybee_energy.construction.window import WindowConstruction
from honeybee_energy.material.opaque import EnergyMaterial, EnergyMaterialNoMass
from honeybee_energy.material.glazing import EnergyWindowMaterialGlazing, \
    EnergyWindowMaterialSimpleGlazSys
from honeybee_energy.material.gas import EnergyWindowMaterialGas, \
    EnergyWindowMaterialGasMixture, EnergyWindowMaterialGasCustom

from honeybee_energy.programtype import ProgramType
from honeybee_energy.schedule.ruleset import ScheduleRuleset

from honeybee_radiance.modifierset import ModifierSet
from honeybee_radiance.modifier import Modifier
from honeybee_radiance.reader import string_to_dicts
from honeybee_radiance.mutil import dict_to_modifier

import json
import pytest


def test_construction_lib():
    """Test that the all of the constructions in the default library can be parsed."""
    constr_default = './honeybee_standards/data/constructions/default.idf'

    opaque_constrs = OpaqueConstruction.extract_all_from_idf_file(constr_default)
    assert len(opaque_constrs[1]) >= 12
    assert len(opaque_constrs[0]) >= 11
    for constr in opaque_constrs[1]:
        assert isinstance(constr, (EnergyMaterial, EnergyMaterialNoMass))
    for constr in opaque_constrs[0]:
        assert isinstance(constr, OpaqueConstruction)

    window_constrs = WindowConstruction.extract_all_from_idf_file(constr_default)
    assert len(window_constrs[1]) >= 4
    assert len(window_constrs[0]) >= 2
    for constr in window_constrs[1]:
        assert isinstance(constr, (EnergyWindowMaterialGlazing,
                                   EnergyWindowMaterialSimpleGlazSys,
                                   EnergyWindowMaterialGas,
                                   EnergyWindowMaterialGasMixture,
                                   EnergyWindowMaterialGasCustom))
    for constr in window_constrs[0]:
        assert isinstance(constr, WindowConstruction)


def test_constructionsets_lib():
    """Test all of the construction sets in the default library."""
    constr_default = './honeybee_standards/data/constructionsets/default.json'
    opaque_cs = OpaqueConstruction.extract_all_from_idf_file(constr_default)
    window_cs = WindowConstruction.extract_all_from_idf_file(constr_default)

    csets = []
    with open(constr_default, 'r') as json_file:
        c_dict = json.load(json_file)
        for c_id in c_dict:
            constructionset = ConstructionSet.from_dict_abridged(
                c_dict[c_id], opaque_cs[0] + window_cs[1])
            csets.append(constructionset)

    assert len(csets) >= 1
    for constr_set in csets:
        assert isinstance(constr_set, ConstructionSet)


def test_schedule_lib():
    """Test that the all of the constructions in the default library can be parsed in."""
    sched_default = './honeybee_standards/data/schedules/default.idf'

    schedule_rulesets = ScheduleRuleset.extract_all_from_idf_file(sched_default)
    assert len(schedule_rulesets) >= 9
    for sched in schedule_rulesets:
        assert isinstance(sched, ScheduleRuleset)


def test_programtype_lib():
    """Test all of the construction sets in the default library."""
    ptype_default = './honeybee_standards/data/programtypes/default.json'
    sched_default = './honeybee_standards/data/schedules/default.idf'
    schedule_rulesets = ScheduleRuleset.extract_all_from_idf_file(sched_default)
    assert len(schedule_rulesets) >= 9
    scheds = {}
    for sched in schedule_rulesets:
        assert isinstance(sched, ScheduleRuleset)
        scheds[sched.identifier] = sched

    ptypes = []
    with open(ptype_default, 'r') as json_file:
        p_dict = json.load(json_file)
        for p_id in p_dict:
            programtype = ProgramType.from_dict_abridged(p_dict[p_id], scheds)
            ptypes.append(programtype)

    assert len(ptypes) >= 2
    for programtype in ptypes:
        assert isinstance(programtype, ProgramType)


def test_modifier_lib():
    """Test that the all of the modifiers in the default library can be parsed in."""
    mod_default = './honeybee_standards/data/modifiers/default.mat'

    modifiers = []
    with open(mod_default) as f:
        rad_dicts = string_to_dicts(f.read())
        for mod_dict in rad_dicts:
            mod = dict_to_modifier(mod_dict)
            modifiers.append(mod)

    assert len(modifiers) >= 19
    for mod in modifiers:
        assert isinstance(mod, Modifier)


def test_modifiersets_lib():
    """Test all of the modifier sets in the default library."""
    modset_default = './honeybee_standards/data/modifiersets/default.json'
    mod_default = './honeybee_standards/data/modifiers/default.mat'
    modifiers = {}
    with open(mod_default) as f:
        rad_dicts = string_to_dicts(f.read())
        for mod_dict in rad_dicts:
            mod = dict_to_modifier(mod_dict)
            modifiers[mod.identifier] = mod

    msets = []
    with open(modset_default, 'r') as json_file:
        m_dict = json.load(json_file)
        for m_id in m_dict:
            modifierset = ModifierSet.from_dict_abridged(m_dict[m_id], modifiers)
            msets.append(modifierset)

    assert len(msets) >= 4
    for mod_set in msets:
        assert isinstance(mod_set, ModifierSet)
