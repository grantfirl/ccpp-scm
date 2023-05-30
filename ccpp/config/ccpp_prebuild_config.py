#!/usr/bin/env python

# CCPP prebuild config for CCPP Single Column Model (SCM)


###############################################################################
# Definitions                                                                 #
###############################################################################

HOST_MODEL_IDENTIFIER = "SCM"

# Add all files with metadata tables on the host model side and in CCPP,
# relative to basedir = top-level directory of host model. This includes
# kind and type definitions used in CCPP physics. Also add any internal
# dependencies of these files to the list.
VARIABLE_DEFINITION_FILES = [
    # actual variable definition files
    'ccpp/framework/src/ccpp_types.F90',
    'ccpp/physics/physics/machine.F',
    'ccpp/physics/physics/radsw_param.f',
    'ccpp/physics/physics/radlw_param.f',
    'ccpp/physics/physics/h2o_def.f',
    'ccpp/physics/physics/ozne_def.f',
    'ccpp/physics/physics/radiation_surface.f',
    'scm/src/CCPP_typedefs.F90',
    'scm/src/GFS_typedefs.F90',
    'scm/src/scm_kinds.F90',
    'scm/src/scm_type_defs.F90',
    'scm/src/scm_physical_constants.F90',
    'scm/src/scm_utils.F90', #no definitions, but scm_type_defs.F90 uses a module from this file
    ]

TYPEDEFS_NEW_METADATA = {
    'ccpp_types' : {
        'ccpp_types' : '',
        'ccpp_t' : 'cdata',
        },
    'machine' : {
        'machine' : '',
        },
    'module_radlw_parameters' : {
        'module_radsw_parameters' : '',
        },
    'module_radlw_parameters' : {
        'module_radlw_parameters' : '',
        },
    'CCPP_typedefs' : {
        'GFS_interstitial_type' : 'physics%Interstitial',
        'CCPP_typedefs' : '',
        },
    'GFS_typedefs' : {
        'GFS_diag_type' : 'physics%Diag',
        'GFS_control_type' : 'physics%Model',
        'GFS_cldprop_type' : 'physics%Cldprop',
        'GFS_tbd_type' : 'physics%Tbd',
        'GFS_sfcprop_type' : 'physics%Sfcprop',
        'GFS_coupling_type' : 'physics%Coupling',
        'GFS_statein_type' : 'physics%Statein',
        'GFS_radtend_type' : 'physics%Radtend',
        'GFS_grid_type' : 'physics%Grid',
        'GFS_stateout_type' : 'physics%Stateout',
        'GFS_typedefs' : '',
        },
    'scm_physical_constants' : {
        'scm_physical_constants' : '',
        },
    'scm_type_defs' : {
        'scm_type_defs' : '',
        'physics_type' : 'physics',
        },
    'module_ccpp_scheme_simulator' : {
        'base_physics_process' : '',
        'module_ccpp_scheme_simulator' : '',
        },
    }

# Add all physics scheme files relative to basedir
SCHEME_FILES = [
    # Relative path to source (from where ccpp_prebuild.py is called) : [ list of physics sets in which scheme may be called ];
    # current restrictions are that each scheme can only belong to one physics set, and all schemes within one group in the
    # suite definition file have to belong to the same physics set
    'ccpp/physics/physics/GFS_DCNV_generic_pre.F90'         ,
    'ccpp/physics/physics/GFS_DCNV_generic_post.F90'        ,
    'ccpp/physics/physics/GFS_GWD_generic_pre.F90'          ,
    'ccpp/physics/physics/GFS_GWD_generic_post.F90'         ,
    'ccpp/physics/physics/GFS_MP_generic_pre.F90'           ,
    'ccpp/physics/physics/GFS_MP_generic_post.F90'          ,
    'ccpp/physics/physics/GFS_PBL_generic_pre.F90'          ,
    'ccpp/physics/physics/GFS_PBL_generic_post.F90'         ,
    'ccpp/physics/physics/GFS_SCNV_generic_pre.F90'         ,
    'ccpp/physics/physics/GFS_SCNV_generic_post.F90'        ,
    'ccpp/physics/physics/GFS_phys_time_vary.scm.F90'       ,
    'ccpp/physics/physics/GFS_rad_time_vary.scm.F90'        ,
    'ccpp/physics/physics/GFS_radiation_surface.F90'        ,
    'ccpp/physics/physics/GFS_rrtmg_post.F90'               ,
    'ccpp/physics/physics/GFS_rrtmg_pre.F90'                ,
    'ccpp/physics/physics/GFS_rrtmg_setup.F90'              ,
    'ccpp/physics/physics/GFS_suite_interstitial_rad_reset.F90',
    'ccpp/physics/physics/GFS_suite_interstitial_phys_reset.F90',
    'ccpp/physics/physics/GFS_suite_interstitial_1.F90'     ,
    'ccpp/physics/physics/GFS_suite_interstitial_2.F90'     ,
    'ccpp/physics/physics/GFS_suite_stateout_reset.F90'     ,
    'ccpp/physics/physics/GFS_suite_stateout_update.F90'    ,
    'ccpp/physics/physics/GFS_suite_interstitial_3.F90'     ,
    'ccpp/physics/physics/GFS_suite_interstitial_4.F90'     ,
    'ccpp/physics/physics/GFS_suite_interstitial_5.F90'     ,
    'ccpp/physics/physics/GFS_surface_generic_pre.F90'      ,
    'ccpp/physics/physics/GFS_surface_generic_post.F90'     ,
    'ccpp/physics/physics/GFS_surface_composites_pre.F90'   ,
    'ccpp/physics/physics/GFS_surface_composites_inter.F90' ,
    'ccpp/physics/physics/GFS_surface_composites_post.F90'  ,
    'ccpp/physics/physics/GFS_surface_loop_control_part1.F90' ,
    'ccpp/physics/physics/GFS_surface_loop_control_part2.F90' ,
    'ccpp/physics/physics/GFS_time_vary_pre.scm.F90'        ,
#    'ccpp/physics/physics/bl_acm.F90'                       ,
    'ccpp/physics/physics/cires_ugwp.F90'                   ,
    'ccpp/physics/physics/cires_ugwp_post.F90'              ,
    'ccpp/physics/physics/unified_ugwp.F90'                 ,
    'ccpp/physics/physics/unified_ugwp_post.F90'            ,
    'ccpp/physics/physics/ugwpv1_gsldrag.F90'               ,
    'ccpp/physics/physics/ugwpv1_gsldrag_post.F90'          ,
    'ccpp/physics/physics/cnvc90.f'                         ,
    'ccpp/physics/physics/cs_conv_pre.F90'                  ,
    'ccpp/physics/physics/cs_conv.F90'                      ,
    'ccpp/physics/physics/cs_conv_post.F90'                 ,
    'ccpp/physics/physics/cs_conv_aw_adj.F90'               ,
    'ccpp/physics/physics/cu_ntiedtke_pre.F90'              ,
    'ccpp/physics/physics/cu_ntiedtke.F90'                  ,
    'ccpp/physics/physics/cu_ntiedtke_post.F90'             ,
    'ccpp/physics/physics/dcyc2t3.f'                        ,
    'ccpp/physics/physics/drag_suite.F90'                   ,
    'ccpp/physics/physics/shoc.F90'                         ,
    'ccpp/physics/physics/get_prs_fv3.F90'                  ,
    'ccpp/physics/physics/get_phi_fv3.F90'                  ,
    'ccpp/physics/physics/gfdl_cloud_microphys.F90'         ,
    'ccpp/physics/physics/gfdl_sfc_layer.F90'               ,
    'ccpp/physics/physics/zhaocarr_gscond.f'                ,
    'ccpp/physics/physics/gwdc_pre.f'                       ,
    'ccpp/physics/physics/gwdc.f'                           ,
    'ccpp/physics/physics/gwdc_post.f'                      ,
    'ccpp/physics/physics/gwdps.f'                          ,
    'ccpp/physics/physics/h2ophys.f'                        ,
    'ccpp/physics/physics/samfdeepcnv.f'                    ,
    'ccpp/physics/physics/samfshalcnv.f'                    ,
    'ccpp/physics/physics/sascnvn.F'                        ,
    'ccpp/physics/physics/shalcnv.F'                        ,
    'ccpp/physics/physics/maximum_hourly_diagnostics.F90'   ,
    'ccpp/physics/physics/m_micro.F90'                      ,
    'ccpp/physics/physics/m_micro_pre.F90'                  ,
    'ccpp/physics/physics/m_micro_post.F90'                 ,
    'ccpp/physics/physics/cu_gf_driver_pre.F90'             ,
    'ccpp/physics/physics/cu_gf_driver.F90'                 ,
    'ccpp/physics/physics/cu_gf_driver_post.F90'            ,
    'ccpp/physics/physics/cu_unified_driver_pre.F90'        ,
    'ccpp/physics/physics/cu_unified_driver.F90'            ,
    'ccpp/physics/physics/cu_unified_driver_post.F90'       ,
    'ccpp/physics/physics/hedmf.f'                          ,
    'ccpp/physics/physics/moninshoc.f'                      ,
    'ccpp/physics/physics/satmedmfvdif.F'                   ,
    'ccpp/physics/physics/satmedmfvdifq.F'                  ,
    'ccpp/physics/physics/shinhongvdif.F90'                 ,
    'ccpp/physics/physics/ysuvdif.F90'                      ,
    'ccpp/physics/physics/mynnedmf_wrapper.F90'             ,
    'ccpp/physics/physics/mynnsfc_wrapper.F90'              ,
    'ccpp/physics/physics/sgscloud_radpre.F90'              ,
    'ccpp/physics/physics/sgscloud_radpost.F90'             ,
    'ccpp/physics/physics/myjsfc_wrapper.F90'               ,
    'ccpp/physics/physics/myjpbl_wrapper.F90'               ,
    'ccpp/physics/physics/mp_thompson_pre.F90'              ,
    'ccpp/physics/physics/mp_thompson.F90'                  ,
    'ccpp/physics/physics/mp_thompson_post.F90'             ,
    'ccpp/physics/physics/mp_nssl.F90'                      ,
    'ccpp/physics/physics/ozphys.f'                         ,
    'ccpp/physics/physics/ozphys_2015.f'                    ,
    'ccpp/physics/physics/zhaocarr_precpd.f'                ,
    'ccpp/physics/physics/phys_tend.F90'                    ,
    'ccpp/physics/physics/radlw_main.F90'                   ,
    'ccpp/physics/physics/radsw_main.F90'                   ,
    'ccpp/physics/physics/rascnv.F90'                       ,
    'ccpp/physics/physics/rayleigh_damp.f'                  ,
    'ccpp/physics/physics/rrtmg_lw_post.F90'                ,
    'ccpp/physics/physics/rrtmg_lw_pre.F90'                 ,
    'ccpp/physics/physics/rrtmg_sw_post.F90'                ,
    'ccpp/physics/physics/rad_sw_pre.F90'                   ,
    'ccpp/physics/physics/sfc_diag.f'                       ,
    'ccpp/physics/physics/sfc_diag_post.F90'                ,
    'ccpp/physics/physics/lsm_ruc.F90'                      ,
    'ccpp/physics/physics/sfc_cice.f'                       ,
    'ccpp/physics/physics/sfc_diff.f'                       ,
    'ccpp/physics/physics/lsm_noah.f'                       ,
    'ccpp/physics/physics/noahmpdrv.F90'                    ,
    'ccpp/physics/physics/flake_driver.F90'                 ,
    'ccpp/physics/physics/sfc_nst_pre.f'                    ,
    'ccpp/physics/physics/sfc_nst.f'                        ,
    'ccpp/physics/physics/sfc_nst_post.f'                   ,
    'ccpp/physics/physics/sfc_ocean.F'                      ,
    'ccpp/physics/physics/sfc_sice.f'                       ,
    'ccpp/physics/physics/mp_fer_hires.F90'                 ,
    # SMOKE
    'ccpp/physics/physics/smoke_dust/rrfs_smoke_wrapper.F90',
    'ccpp/physics/physics/smoke_dust/rrfs_smoke_postpbl.F90',
    'ccpp/physics/physics/scm_sfc_flux_spec.F90'            ,
    # RRTMGP
    'ccpp/physics/physics/rrtmgp_aerosol_optics.F90'        ,
    'ccpp/physics/physics/rrtmgp_lw_main.F90'                ,
    'ccpp/physics/physics/rrtmgp_sw_main.F90'                ,
    'ccpp/physics/physics/GFS_rrtmgp_setup.F90'             ,
    'ccpp/physics/physics/GFS_rrtmgp_pre.F90'               ,
    'ccpp/physics/physics/GFS_cloud_diagnostics.F90'        ,
    'ccpp/physics/physics/GFS_rrtmgp_cloud_mp.F90'          ,
    'ccpp/physics/physics/GFS_rrtmgp_cloud_overlap.F90'     ,
    'ccpp/physics/physics/GFS_rrtmgp_post.F90'              ,
    'ccpp/physics/physics/GFS_ccpp_scheme_sim_pre.F90'      ,
    'ccpp/physics/physics/ccpp_scheme_simulator.F90'
    ]

# Default build dir, relative to current working directory,
# if not specified as command-line argument
DEFAULT_BUILD_DIR = 'scm/bin'

# Auto-generated makefile/cmakefile snippets that contain all type definitions
TYPEDEFS_MAKEFILE   = '{build_dir}/ccpp/physics/CCPP_TYPEDEFS.mk'
TYPEDEFS_CMAKEFILE  = '{build_dir}/ccpp/physics/CCPP_TYPEDEFS.cmake'
TYPEDEFS_SOURCEFILE = '{build_dir}/ccpp/physics/CCPP_TYPEDEFS.sh'

# Auto-generated makefile/cmakefile snippets that contain all schemes
SCHEMES_MAKEFILE = '{build_dir}/ccpp/physics/CCPP_SCHEMES.mk'
SCHEMES_CMAKEFILE = '{build_dir}/ccpp/physics/CCPP_SCHEMES.cmake'
SCHEMES_SOURCEFILE = '{build_dir}/ccpp/physics/CCPP_SCHEMES.sh'

# Auto-generated makefile/cmakefile snippets that contain all caps
CAPS_MAKEFILE = '{build_dir}/ccpp/physics/CCPP_CAPS.mk'
CAPS_CMAKEFILE = '{build_dir}/ccpp/physics/CCPP_CAPS.cmake'
CAPS_SOURCEFILE = '{build_dir}/ccpp/physics/CCPP_CAPS.sh'

# Directory where to put all auto-generated physics caps
CAPS_DIR = '{build_dir}/ccpp/physics/physics'

# Directory where the suite definition files are stored
SUITES_DIR = 'ccpp/suites'

# Directory where to write static API to
STATIC_API_DIR = 'scm/src/'
STATIC_API_CMAKEFILE = 'scm/src/CCPP_STATIC_API.cmake'
STATIC_API_SOURCEFILE = 'scm/src/CCPP_STATIC_API.sh'

# Directory for writing HTML pages generated from metadata files
METADATA_HTML_OUTPUT_DIR = 'ccpp/physics/physics/docs'

# HTML document containing the model-defined CCPP variables
HTML_VARTABLE_FILE = 'ccpp/physics/CCPP_VARIABLES_SCM.html'

# LaTeX document containing the provided vs requested CCPP variables
LATEX_VARTABLE_FILE = 'ccpp/framework/doc/DevelopersGuide/CCPP_VARIABLES_SCM.tex'
