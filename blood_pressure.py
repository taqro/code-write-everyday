{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "blood_pressure.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMkz08zCQoED/voQKmbzDuQ",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/blood_pressure.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Uz1cxB11ZoJ_",
        "outputId": "71bd169f-36d6-4c5b-db00-b9b85a851c7c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "300 50\n",
            "133.33333333333331\n"
          ]
        }
      ],
      "source": [
        "# 入力\n",
        "A, B = map(int, input().split())\n",
        "\n",
        "C = (A - B) / 3 + B\n",
        "\n",
        "print(C)\n"
      ]
    }
  ]
}