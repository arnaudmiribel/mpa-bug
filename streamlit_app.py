from pathlib import Path

import streamlit as st
from streamlit.source_util import (
    _on_pages_changed,
    calc_md5,
    get_pages,
    page_icon_and_name,
)


def delete_page(main_script_path_str, page_name):
    """
    Function to remove a page from the sidebar navigation.

    Parameters
    ----------
    main_script_path_str : str
        Main page, the .py file used to run the app (Example: streamlit run file.py)
    page_name : str
        The name of the page which must be added back

    """
    current_pages = get_pages(main_script_path_str)

    for key, value in current_pages.items():
        if value["page_name"] == page_name:
            del current_pages[key]
            break
        else:
            pass
    _on_pages_changed.send()


def add_page(main_script_path_str, page_name):
    """
    Function to add back a removed page to the sidebar navigation. The page must exist in the `pages` folder.

    Parameters
    ----------
    main_script_path_str : str
        Main page, the .py file used to run the app (Example: streamlit run file.py)
    page_name : str
        The name of the page which must be added back

    """
    pages = get_pages(main_script_path_str)
    main_script_path = Path(main_script_path_str)
    pages_dir = main_script_path.parent / "pages"
    script_path = [f for f in pages_dir.glob("*.py") if f.name.find(page_name) != -1][0]
    script_path_str = str(script_path.resolve())
    pi, pn = page_icon_and_name(script_path)
    psh = calc_md5(script_path_str)
    pages[psh] = {
        "page_script_hash": psh,
        "page_name": pn,
        "icon": pi,
        "script_path": script_path_str,
    }
    _on_pages_changed.send()


if st.button("Delete Mike"):
    delete_page("streamlit_app.py", "Mike")

if st.button("Delete Albert"):
    delete_page("streamlit_app.py", "Albert")

if st.checkbox("Did you check this or not..."):
    st.write("Wow")
