{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "plural_form.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMMxB2BbEKJHUpXxlNX0WeS",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/plural_form.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Iqlr8OkFs5eZ",
        "outputId": "4403c843-cb76-4769-b95d-03702642e7fd"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "bus\n",
            "buses\n"
          ]
        }
      ],
      "source": [
        "S = list(input())\n",
        "\n",
        "if S[len(S) - 1] == \"s\":\n",
        "  S.append(\"es\")\n",
        "else:\n",
        "  S.append(\"s\")\n",
        "\n",
        "ans = \"\"\n",
        "for i in S:\n",
        "  ans += i\n",
        "\n",
        "print(ans)"
      ]
    }
  ]
}