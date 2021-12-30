{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "determinant.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNltLOF2KG1LI/YZ1AJ2DZo",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/determinant.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "t2kRAk5eOzpf",
        "outputId": "4526bc0a-a1cd-4717-cab8-d943fceabe57"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 2\n",
            "3 4\n",
            "-2\n"
          ]
        }
      ],
      "source": [
        "a, b = map(int, input().split())\n",
        "c, d = map(int, input().split())\n",
        "\n",
        "print(a * d - b * c)"
      ]
    }
  ]
}