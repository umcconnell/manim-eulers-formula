# manim-eulers-formula

Sample manim project animating Euler's formula.


https://user-images.githubusercontent.com/50373698/177876040-aa2ea440-7022-4e0b-a23d-95e8026817ad.mp4


## Table of Contents

- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Initial Setup](#initial-setup)
- [Running](#running)
    - [Concatenation](#concatenation)
    - [Docker](#docker)
- [Authors](#authors)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Getting Started

### Prerequisites

You will need python3 and pip3 installed on your machine. You can install it
from the official website https://www.python.org/.

Additionally, ffmpeg is required to generate and concatenate the individual
scenes. Install ffmepg from https://ffmpeg.org/.

Furthermore, LaTeX is needed to generate the texts and formulas. TeX Live is a
good choice and can be installed from https://www.tug.org/texlive/. A detailed
guide on installing LaTeX on Windows, Mac and Linux can be found in this
document from NYU: https://guides.nyu.edu/LaTeX/installation.

### Initial Setup

A step by step guide to set up a development environment on your local machine.
It is also possible to generate the videos using docker containers. Refer to the
[relevant manim docs](https://docs.manim.community/en/stable/installation.html#using-manim-via-docker)
and the [instructions below](#docker) to learn more.

Clone the git repository:

```bash
git clone https://github.com/umcconnell/manim-eulers-formula.git
cd python-boilerplate-demo/
```

Then create your virtual environment and install the required dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
python3 -m pip install manim
```

To exit the virtual environment run

```bash
deactivate
```

Happy coding!

## Running

Individual video scenes are generated using the manim CLI. The easiest way to
start using the CLI is through the interactive mode by running:

```bash
manim -qh -p main.py 
```

This allows for a selection of scenes present in `main.py` to be rendered in
high quality (`-qh`). Due to rendering speed, medium quality (`-qm`) is
recommended during development.

The manim docs provide a good overview of the CLI and possible flags:
https://docs.manim.community/en/stable/tutorials/configuration.html#command-line-arguments

### Concatenation

To concatenate the different partial scenes into a final output video, use
ffmpeg. Note that the [partial_videos](./partial_videos) file might need to be
edited to reflect different scenes or quality settings:

```bash
ffmpeg -f concat -safe 0 -i partial_videos -c copy output.mp4
```

### Docker

To generate videos without directly installing manim, the docker image
`manimcommunity/manim` can be used instead. Run the following command from the
project root:

```bash
docker run --rm -it -v "$PWD:/manim" manimcommunity/manim manim -qh main.py
```

If you are using podman, use this command instead:

```bash
podman run --rm -it -u root -v "$PWD/:/manim:Z" manimcommunity/manim manim -qh main.py
```

## Authors

Ulysse McConnell - [umcconnell](https://github.com/umcconnell/)

See also the list of
[contributors](https://github.com/umcconnell/manim-eulers-formula/contributors)
who participated in this project.

## License

This project is licensed under the MIT License - see the
[LICENSE.md](./LICENSE.md) file for details.

## Acknowledgments

- [Benjamin Hackl's tutorial series "Mathematical Animations WITH EASE" on YouTube](https://www.youtube.com/playlist?list=PLsMrDyoG1sZm6-jIUQCgN3BVyEVOZz3LQ)
- https://docs.manim.community/en/stable/
