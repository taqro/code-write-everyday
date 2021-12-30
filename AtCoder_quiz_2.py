{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "AtCoder_quiz_2.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPuen92sj3EHAWU7Da74QN0",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/AtCoder_quiz_2.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "59MMvEpf4q7r",
        "outputId": "05f44739-c307-4ace-ecda-bf9c1ba7186f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0\n",
            "40\n"
          ]
        }
      ],
      "source": [
        "# 入力\n",
        "X = int(input())\n",
        "\n",
        "res = 0\n",
        "if X < 40:\n",
        "  res = 40 - X\n",
        "  print(res)\n",
        "elif 40 <= X < 70:\n",
        "  res = 70 - X\n",
        "  print(res)\n",
        "elif 70 <= X < 90:\n",
        "  res = 90 - X\n",
        "  print(res)\n",
        "else:\n",
        "  print(\"expert\")\n",
        "\n",
        "\n",
        "\n"
      ]
    }
  ]
}