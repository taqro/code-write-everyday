{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "registration.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPFmNdTyiKeneDPEHCoW+6/",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/registration.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "a_aCRrfo2gXw",
        "outputId": "7c1ee653-31e1-4395-f952-02ebdedbd6d7"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "chokudai\n",
            "chokudaiz\n",
            "Yes\n"
          ]
        }
      ],
      "source": [
        "S = list(input())\n",
        "T = list(input())\n",
        "\n",
        "ans = \"Yes\"\n",
        "T.pop()\n",
        "\n",
        "if S != T:\n",
        "  ans = \"No\"\n",
        "\n",
        "print(ans)"
      ]
    }
  ]
}