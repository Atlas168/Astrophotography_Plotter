# Astrophotography Plotter
**A plotter which gets the altitudes for astrophotography targets based on a user-specified date and plotting style.**

## Features
- Computes the altitude of common astrophotography targets over a given night
- Supports multiple and single target plotting modes
- Includes a moon luminance bar
- Contains editable preset lists of targets
  
The targets shown for "multiple" plots are dependent on the season the input month falls into.

## Requirements
This project uses several Python libraries, including:
- **astropy** for unit transformations and altitude values
- **ephem** for moon luminance
- **numpy** for calculations and arrangement
- **matplotlib** for visualization
- **termcolor** for console styling

To install these dependencies, run the following command in a console:

*pip install astropy ephem numpy matplotlib termcolor*

## To Run
Open the Main file and input your:
- latitude
- longitude
- altitude
- UTC offset

into the provided variables. 

Then, simply run the main file and answer the prompts. 

### Customizing Targets
To change the targets plotted for each season, edit the TargetLogic file and input the names of the desired objects. 

*By default, the targets are high-altitude objects in the northern hemisphere.*

## Example Plot
Below is the "multiple" target plot for 2 December 2025.

<img width="936" height="504" alt="Plotter Example 2 (better)" src="https://github.com/user-attachments/assets/f4a2383c-ff95-437c-9b1e-859f46579546" />

## Motivation
As someone who lives in an area filled with tall trees, most of my astrophotography preparation required manually gathering the altitudes of any objects I wanted to image to make sure they were above the tree line. I created this program to streamline this process by automatically computing altitudes and displaying them in an easy-to-read chart. With features including a moon luminance bar and seasonal target selection, this program attempts to reduce the uncertainties which make planning astrophotography difficult, even if it can't stop clouds from ruining a good session.

## Acknowledgement
This program was built using astropy's tutorial ["Determining and plotting the altitude/azimuth of a celestial object"](https://docs.astropy.org/en/latest/coordinates/example_gallery_plot_obs_planning.html) as a starting point.
