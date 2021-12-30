{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "napsack_2.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPX9ChMw54izS9Anxi4my88",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/napsack_2.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XkEs3FAEFSvW",
        "outputId": "62e96306-d67a-4292-dcf9-d7fdbebdcde2"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "N,Wをそれぞれ入力\n",
            "6 9\n",
            "weight,valueのペアを入力\n",
            "2 3\n",
            "1 2\n",
            "3 6\n",
            "2 1\n",
            "1 3\n",
            "5 85\n",
            "94\n"
          ]
        }
      ],
      "source": [
        "# きちんと動く\n",
        "\n",
        "# 入力\n",
        "print(\"N,Wをそれぞれ入力\")\n",
        "N,W = map(int,input().split())\n",
        "\n",
        "w = []\n",
        "v = []\n",
        "\n",
        "#weightとvalueの値を入力\n",
        "print(\"weight,valueのペアを入力\")\n",
        "for i in range(N):\n",
        "    x,y = map(int,input().split())\n",
        "    w.append(x)\n",
        "    v.append(y)\n",
        "\n",
        "# DPテーブルの作成\n",
        "dp = [[0]*(W+1) for j in range(N+1)] \n",
        "\n",
        "for i in range(N):\n",
        "    for j in range(W+1):\n",
        "        if j < w[i]: # 選ばない時\n",
        "            dp[i+1][j] = dp[i][j]\n",
        "        else: # 選ぶ時\n",
        "            dp[i+1][j] = max(dp[i][j],dp[i][j-w[i]]+v[i])\n",
        "\n",
        "# 結果を出力\n",
        "print(dp[N][W])"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "vZXiMRQhFai-"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}