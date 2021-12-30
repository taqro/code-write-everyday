{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "AATCoder.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNNqoHdJdYbJn0zqduanfsw",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/AATCoder.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xm-4cZaRlMiu",
        "outputId": "87ca0dcf-8e04-4467-9054-3d5adf0a91a9"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "SHINJUKU\n",
            "0\n"
          ]
        }
      ],
      "source": [
        "S = list(input())\n",
        "\n",
        "flag = 0\n",
        "length = 0\n",
        "maxlen = 0\n",
        "\n",
        "for i in range(len(S)):\n",
        "  if S[i] == \"A\":\n",
        "    length += 1\n",
        "    flag = 1\n",
        "  elif S[i] == \"C\":\n",
        "    length += 1\n",
        "    flag = 1\n",
        "  elif S[i] == \"G\":\n",
        "    length += 1\n",
        "    flag = 1\n",
        "  elif S[i] == \"T\":\n",
        "    length += 1\n",
        "    flag = 1\n",
        "  else:\n",
        "    flag = 0\n",
        "    \n",
        "  if maxlen < length:\n",
        "    maxlen = length\n",
        "  \n",
        "  if flag == 0:\n",
        "    length = 0\n",
        "\n",
        "print(maxlen)\n",
        "\n",
        "\n"
      ]
    }
  ]
}