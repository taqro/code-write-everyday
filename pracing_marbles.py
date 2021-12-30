{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "pracing_marbles.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMsyfd9r0rDmphT2LtNchhR",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/pracing_marbles.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 12,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gFcwp5wRoujL",
        "outputId": "3eb6e43b-9241-4801-ec44-eed743297bf8"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "０，1のみの三桁の数字を入力\n",
            "001\n",
            "001\n",
            "1は1個含まれています。\n"
          ]
        }
      ],
      "source": [
        "# 入力\n",
        "print(\"０，1のみの三桁の数字を入力\")\n",
        "s = input()\n",
        "print(s)\n",
        "\n",
        "# sumの宣言\n",
        "sum = 0\n",
        "\n",
        "for i in range(0, len(s)):\n",
        "  if s[i] == \"1\": #1はstringであることに注意\n",
        "    sum += 1\n",
        "\n",
        "print(\"1は\" +str(sum) + \"個含まれています。\")\n"
      ]
    }
  ]
}