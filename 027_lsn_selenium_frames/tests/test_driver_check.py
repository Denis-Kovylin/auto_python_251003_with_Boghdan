# tests/test_driver_check.py
def test_driver_opens_page_and_finds_frame(driver):
    frame = driver.find_element("id", "frame1")
    assert frame is not None
