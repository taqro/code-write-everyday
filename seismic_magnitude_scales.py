{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "seismic_magnitude_scales.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNmY9Xl0AmhmbvP/fKRXwfF",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/seismic_magnitude_scales.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tB88mAIo2i8v",
        "outputId": "3d307dcd-17d5-4e67-c316-0e7f20385bdb"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5 5\n",
            "1\n"
          ]
        }
      ],
      "source": [
        "# 入力\n",
        "A, B = map(int, input().split())\n",
        "\n",
        "res = 32 ** (A- B)\n",
        "print(res)"
      ]
    }
  ]
}