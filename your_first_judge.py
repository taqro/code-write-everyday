{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "your_first_judge.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyM5+zqFBQiQrcDjohM205A2",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/your_first_judge.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zoYDGpKo-nTH",
        "outputId": "67eaac2e-0451-4837-eb8b-d17b073f0b94"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hello,World!\n",
            "AC\n"
          ]
        }
      ],
      "source": [
        "# 入力\n",
        "S = list(input())\n",
        "\n",
        "T = list(\"Hello,World!\")\n",
        "\n",
        "ans = \"AC\"\n",
        "\n",
        "if len(S) != len(T):\n",
        "  ans = \"WA\"\n",
        "else:\n",
        "  for i in range(len(S)):\n",
        "    if S[i] != T[i]:\n",
        "      ans = \"WA\"\n",
        "\n",
        "print(ans)"
      ]
    }
  ]
}