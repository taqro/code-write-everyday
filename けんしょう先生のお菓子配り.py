{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "けんしょう先生のお菓子配り.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMtk9B5qAfL3wAIOzPYwmX8",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/%E3%81%91%E3%82%93%E3%81%97%E3%82%87%E3%81%86%E5%85%88%E7%94%9F%E3%81%AE%E3%81%8A%E8%8F%93%E5%AD%90%E9%85%8D%E3%82%8A.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "R2Zt2-nAe9fc",
        "outputId": "89875551-4ef2-4eb8-ebde-e62a6a79aa17"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5\n",
            "5\n",
            "0\n"
          ]
        }
      ],
      "source": [
        "a = int(input())\n",
        "b = int(input())\n",
        "\n",
        "for i in range(100):\n",
        "  if (a + i) % b == 0:\n",
        "    print(i)\n",
        "    break"
      ]
    }
  ]
}