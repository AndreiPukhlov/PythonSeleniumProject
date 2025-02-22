from pprint import pprint

import pytest
import requests

jsn = {
    "locale": {
        "country": "us",
        "attr": "en-US",
        "textDirection": "ltr"
    },
    "localeswitcher": {
        "name": "localeswitcher",
        "metadata": {},
        "displayIndex": 0,
        "copy": {
            "name": "copy",
            "metadata": {},
            "displayIndex": 0,
            "value": "Choose another country or region to see content specific to your location and shop online.",
            "path": "ac-localeswitcher.localeswitcher.localeswitcher.copy"
        },
        "continue": {
            "name": "continue",
            "metadata": {},
            "displayIndex": 1,
            "value": "Continue",
            "path": "ac-localeswitcher.localeswitcher.localeswitcher.continue"
        },
        "exit": {
            "name": "exit",
            "metadata": {
                "duration": "30",
                "dismiss": "1"
            },
            "displayIndex": 2,
            "value": "Close country or region selector",
            "path": "ac-localeswitcher.localeswitcher.localeswitcher.exit"
        },
        "select": {
            "name": "select",
            "metadata": {},
            "displayIndex": 0,
            "suggestion1": {
                "name": "suggestion1",
                "metadata": {},
                "displayIndex": 0,
                "value": "United States",
                "path": "ac-localeswitcher.localeswitcher.localeswitcher.select.suggestion1"
            },
            "choose": {
                "name": "choose",
                "metadata": {
                    "url": "https://www.apple.com/choose-country-region/"
                },
                "displayIndex": 1,
                "value": "Other country or region",
                "path": "ac-localeswitcher.localeswitcher.localeswitcher.select.choose"
            },
            "path": "ac-localeswitcher.localeswitcher.localeswitcher.select"
        },
        "wrapper": {
            "name": "wrapper",
            "metadata": {},
            "displayIndex": 2,
            "label": {
                "name": "label",
                "metadata": {},
                "displayIndex": 0,
                "value": "Choose country or region",
                "path": "ac-localeswitcher.localeswitcher.localeswitcher.wrapper.label"
            },
            "path": "ac-localeswitcher.localeswitcher.localeswitcher.wrapper"
        },
        "path": "ac-localeswitcher.localeswitcher.localeswitcher"
    }
}


def test_get():
    var = requests.get("https://www.apple.com/ac/localeswitcher/4/en_US/content/localeswitcher.json")
    pprint(var.status_code, indent=4)
    # pprint(var.json(), indent=4)
    assert var.json().__eq__(jsn)
    assert var.json()["locale"] == {'country': 'us', 'attr': 'en-US', 'textDirection': 'ltr'}
