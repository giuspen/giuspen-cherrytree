#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from __future__ import absolute_import
from __future__ import print_function

# __author__ = 'Jakub Kolasa <jakub@arker.pl'>

UI_INFO_STRUCT_MENUBAR = [['MenuBar',
  [['FileMenu',
    ['ct_new_inst',
     'ct_open_file',
     '-',
     'ct_vacuum',
     'ct_save',
     'ct_save_as',
     '-',
     'print_page_setup',
     'do_print',
     '-',
     'exec_code',
     '-',
     'quit_app',
     'exit_app']],
   ['EditMenu',
    ['preferences_dlg',
     '-',
     'act_undo',
     'act_redo',
     '-',
     'handle_image',
     'handle_table',
     'handle_codebox',
     'handle_embfile',
     'handle_link',
     'handle_anchor',
     'insert_toc',
     'insert_timestamp',
     'insert_horiz_rule',
     'strip_trail_spaces',
     '-',
     ['ChangeCaseMenu', ['case_down', 'case_up', 'case_tggl']],
     '-',
     'spellcheck_toggle',
     '-',
     'cut_plain',
     'copy_plain',
     'paste_plain',
     '-',
     'cut_row',
     'copy_row',
     'del_row',
     'dup_row',
     'mv_up_row',
     'mv_down_row']],
   ['FormattingMenu',
    ['fmt_latest',
     'fmt_rm',
     '-',
     'fmt_color_fg',
     'fmt_color_bg',
     'fmt_bold',
     'fmt_italic',
     'fmt_underline',
     'fmt_strikethrough',
     'fmt_h1',
     'fmt_h2',
     'fmt_h3',
     'fmt_small',
     'fmt_superscript',
     'fmt_subscript',
     'fmt_monospace',
     '-',
     'handle_bull_list',
     'handle_num_list',
     'handle_todo_list',
     '-',
     'fmt_justify_left',
     'fmt_justify_center',
     'fmt_justify_right',
     'fmt_justify_fill']],
   ['TreeMenu', []],
   ['SearchMenu',
    ['find_in_node',
     'find_in_allnodes',
     'find_in_node_n_sub',
     'find_in_node_names',
     'find_iter_fw',
     'find_iter_bw',
     '-',
     'replace_in_node',
     'replace_in_allnodes',
     'replace_in_node_n_sub',
     'replace_in_node_names',
     'replace_iter_fw']],
   ['ViewMenu',
    ['toggle_show_tree',
     'toggle_show_toolbar',
     'toggle_show_node_name_head',
     'toggle_show_allmatches_dlg',
     '-',
     'toggle_focus_tree_text',
     'nodes_all_expand',
     'nodes_all_collapse',
     '-',
     'toolbar_icons_size_p',
     'toolbar_icons_size_m',
     '-',
     'toggle_fullscreen']],
   ['BookmarksMenu', ['handle_bookmarks']],
   ['ImportMenu',
    ['import_cherrytree',
     'import_txt_file',
     'import_txt_folder',
     'import_html_file',
     'import_html_folder',
     'import_basket',
     'import_epim_html',
     'import_gnote',
     'import_keepnote',
     'import_keynote',
     'import_knowit',
     'import_leo',
     'import_mempad',
     'import_notecase',
     'import_rednotebook',
     'import_tomboy',
     'import_treepad',
     'import_tuxcards',
     'import_zim']],
   ['ExportMenu',
    ['export_pdf',
     'export_html',
     'export_txt_multiple',
     'export_txt_single',
     'export_ctd']],
   ['HelpMenu',
    ['ct_check_newer',
     '-',
     'ct_help',
     '-',
     'open_cfg_folder',
     '-',
     'ct_about']]]]]
UI_INFO_STRUCT_POPUP = [['SysTrayMenu', ['toggle_show_mainwin', '-', 'exit_app']],
 ['ImageMenu',
  ['img_cut',
   'img_copy',
   'img_del',
   '-',
   'img_edit',
   'img_save',
   '-',
   'img_link_edit',
   'img_link_dismiss']],
 ['AnchorMenu', ['anch_cut', 'anch_copy', 'anch_del', '-', 'anch_edit']],
 ['EmbFileMenu',
  ['emb_file_cut',
   'emb_file_copy',
   'emb_file_del',
   '-',
   'emb_file_open',
   'emb_file_save']]]