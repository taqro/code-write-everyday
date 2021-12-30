{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "circle_pond.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMYAltIW7Vs13qrLDvcbmhN",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/circle_pond.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kxhyEeV1IvpY",
        "outputId": "82d95d50-bc2b-44b2-b483-e295253d1eb0"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n",
            "6.283185307179586\n"
          ]
        }
      ],
      "source": [
        "import math\n",
        "\n",
        "R = int(input())\n",
        "ans = 2 * math.pi * R\n",
        "\n",
        "print(ans)"
      ]
    }
  ]
}