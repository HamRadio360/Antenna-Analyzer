![Ham Radio 360 Logo](http://www.360workbench.com/wpimages/wp9fedbb3f_06.png "Ham Radio 360 Logo") ![Workbench Podcast Logo](http://www.360workbench.com/wpimages/wp02796e2d_06.png "Workbench Logo")

# Firmware

Contained in this directory are two versions of the firmware. The original - "aa_firmware_v1", and the user-improved version.

The user-improved version currently has these changes and/or additional features:

* Scrolling boot screen
* Debounced the BAND button
* Pressing the BAND button puts it into a mode where it waits five seconds for the user to press it again before starting a scan. This allows much quicker selection of the band. The cursor flashes during this band-selection mode.
* Pressing the BAND button will interrupt the sweep/scan to allow quicker band selection
* During the scan, it shows a rough plot of the VSWR which also acts as a progress bar for the scan
* The frequency display is now in MHz and rounded to six digits.
* VSWR is shown with one digit of precision so it fits on the display without pushing anything off the edge
