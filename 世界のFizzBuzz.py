{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "世界のFizzBuzz.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPY460SOjoFU8MMBEF4arLH",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/%E4%B8%96%E7%95%8C%E3%81%AEFizzBuzz.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eH7VfFDoXyjW",
        "outputId": "f953ba3f-8d54-419d-df37-20fa39c087e5"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "4\n",
            "N0\n"
          ]
        }
      ],
      "source": [
        "N = int(input())\n",
        "\n",
        "if N % 3 == 0:\n",
        "  print(\"YES\")\n",
        "else:\n",
        "  print(\"NO\")"
      ]
    }
  ]
}