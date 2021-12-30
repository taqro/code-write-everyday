{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "rainy_season.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPSE0oplXFtTMg532VYTnUw",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/rainy_season.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "H36MeFNzwgSc",
        "outputId": "fb02d241-3b06-4bfc-a299-9bd3c1142d3c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "RSR\n",
            "1\n"
          ]
        }
      ],
      "source": [
        "S = list(input())\n",
        "\n",
        "sum = 0\n",
        "ans = 0\n",
        "\n",
        "for i in range(3):\n",
        "  if S[i] == \"R\":\n",
        "    sum += 1\n",
        "    if sum > ans:\n",
        "      ans = sum\n",
        "  else:\n",
        "    sum =  0\n",
        "\n",
        "print(ans)"
      ]
    }
  ]
}