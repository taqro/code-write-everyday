{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "first_grid.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMrucWG6CmDn0rfeofWf5Z7",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/first_grid.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WAGgExUAYRiQ",
        "outputId": "5445a2f4-450c-4a9b-ced4-3cb5ac5fa922"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            ".#\n",
            "#.\n",
            "No\n"
          ]
        }
      ],
      "source": [
        "# 入力\n",
        "S_1 = list(input())\n",
        "S_2 = list(input())\n",
        "\n",
        "res = \"Yes\"\n",
        "\n",
        "if S_1[0] == \".\" and S_2[1] == \".\":\n",
        "  res = \"No\"\n",
        "\n",
        "if S_1[1] == \".\" and S_2[0] == \".\":\n",
        "  res = \"No\"\n",
        "\n",
        "print(res)\n",
        "\n",
        "\n",
        "\n"
      ]
    }
  ]
}