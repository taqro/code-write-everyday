{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "papers_please.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNXIqP6QjJSyXeH3Gj/XkDs",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/papers_please.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Sp41XFAGHFAn",
        "outputId": "f71e3361-f1f7-4a2f-e715-c0913b6a1763"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3\n",
            "28 27 24\n",
            "DENIED\n"
          ]
        }
      ],
      "source": [
        "#入力\n",
        "N = int(input())\n",
        "a = list(map(int, input().split()))\n",
        "result = \"APPROVED\"\n",
        "\n",
        "for i in range(N):\n",
        "  if a[i] % 2 == 0:\n",
        "    if a[i] % 3 == 0 or a[i] % 5 == 0:\n",
        "      continue\n",
        "    else:\n",
        "      result = \"DENIED\"\n",
        "\n",
        "print(result)"
      ]
    }
  ]
}