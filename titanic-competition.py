{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "3fd7c6e4",
   "metadata": {
    "papermill": {
     "duration": 0.026246,
     "end_time": "2022-01-23T10:46:15.254334",
     "exception": false,
     "start_time": "2022-01-23T10:46:15.228088",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "### Titanic Competition Presented By Edeh Emeka N. (Second Submission)\n",
    "\n",
    "\n",
    "#### **The Challenge**\n",
    "The sinking of the Titanic is one of the most infamous shipwrecks in history.\n",
    "\n",
    "On April 15, 1912, during her maiden voyage, the widely considered “unsinkable” RMS Titanic sank after colliding with an iceberg. Unfortunately, there weren’t enough lifeboats for everyone onboard, resulting in the death of 1502 out of 2224 passengers and crew.\n",
    "\n",
    "While there was some element of luck involved in surviving, it seems some groups of people were more likely to survive than others.\n",
    "\n",
    "In this challenge, we ask you to build a predictive model that answers the question: **“what sorts of people were more likely to survive?”** using passenger data (ie name, age, gender, socio-economic class, etc)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "da62c229",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-23T10:46:15.313214Z",
     "iopub.status.busy": "2022-01-23T10:46:15.312584Z",
     "iopub.status.idle": "2022-01-23T10:46:16.267558Z",
     "shell.execute_reply": "2022-01-23T10:46:16.266856Z",
     "shell.execute_reply.started": "2022-01-23T10:41:15.642797Z"
    },
    "papermill": {
     "duration": 0.988962,
     "end_time": "2022-01-23T10:46:16.267722",
     "exception": false,
     "start_time": "2022-01-23T10:46:15.278760",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "import math\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "55c5613b",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-23T10:46:16.319772Z",
     "iopub.status.busy": "2022-01-23T10:46:16.318782Z",
     "iopub.status.idle": "2022-01-23T10:46:16.357762Z",
     "shell.execute_reply": "2022-01-23T10:46:16.357087Z",
     "shell.execute_reply.started": "2022-01-23T10:41:39.745868Z"
    },
    "papermill": {
     "duration": 0.066214,
     "end_time": "2022-01-23T10:46:16.357907",
     "exception": false,
     "start_time": "2022-01-23T10:46:16.291693",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "titanic_train = pd.read_csv(\"../input/titaniccsv/titanic.csv\")\n",
    "titanic_test = pd.read_csv(\"../input/titaniccsv/test.csv\")\n",
    "test_ids = titanic_test[\"PassengerId\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "ec427387",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-23T10:46:16.413140Z",
     "iopub.status.busy": "2022-01-23T10:46:16.412557Z",
     "iopub.status.idle": "2022-01-23T10:46:16.429953Z",
     "shell.execute_reply": "2022-01-23T10:46:16.430462Z",
     "shell.execute_reply.started": "2022-01-23T10:41:45.873332Z"
    },
    "papermill": {
     "duration": 0.048258,
     "end_time": "2022-01-23T10:46:16.430637",
     "exception": false,
     "start_time": "2022-01-23T10:46:16.382379",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Cabin</th>\n",
       "      <th>Embarked</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Braund, Mr. Owen Harris</td>\n",
       "      <td>male</td>\n",
       "      <td>22.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>A/5 21171</td>\n",
       "      <td>7.2500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>\n",
       "      <td>female</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>PC 17599</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>C85</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>Heikkinen, Miss. Laina</td>\n",
       "      <td>female</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>STON/O2. 3101282</td>\n",
       "      <td>7.9250</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>\n",
       "      <td>female</td>\n",
       "      <td>35.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>113803</td>\n",
       "      <td>53.1000</td>\n",
       "      <td>C123</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Allen, Mr. William Henry</td>\n",
       "      <td>male</td>\n",
       "      <td>35.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>373450</td>\n",
       "      <td>8.0500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   PassengerId  Survived  Pclass  \\\n",
       "0            1         0       3   \n",
       "1            2         1       1   \n",
       "2            3         1       3   \n",
       "3            4         1       1   \n",
       "4            5         0       3   \n",
       "\n",
       "                                                Name     Sex   Age  SibSp  \\\n",
       "0                            Braund, Mr. Owen Harris    male  22.0      1   \n",
       "1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   \n",
       "2                             Heikkinen, Miss. Laina  female  26.0      0   \n",
       "3       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1   \n",
       "4                           Allen, Mr. William Henry    male  35.0      0   \n",
       "\n",
       "   Parch            Ticket     Fare Cabin Embarked  \n",
       "0      0         A/5 21171   7.2500   NaN        S  \n",
       "1      0          PC 17599  71.2833   C85        C  \n",
       "2      0  STON/O2. 3101282   7.9250   NaN        S  \n",
       "3      0            113803  53.1000  C123        S  \n",
       "4      0            373450   8.0500   NaN        S  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "titanic_train.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4427f4d2",
   "metadata": {
    "papermill": {
     "duration": 0.02425,
     "end_time": "2022-01-23T10:46:16.480054",
     "exception": false,
     "start_time": "2022-01-23T10:46:16.455804",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## EDA (Understanding the given train dataset)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "c5752770",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-23T10:46:16.533362Z",
     "iopub.status.busy": "2022-01-23T10:46:16.532417Z",
     "iopub.status.idle": "2022-01-23T10:46:16.537097Z",
     "shell.execute_reply": "2022-01-23T10:46:16.537612Z",
     "shell.execute_reply.started": "2022-01-23T10:41:50.643129Z"
    },
    "papermill": {
     "duration": 0.03275,
     "end_time": "2022-01-23T10:46:16.537769",
     "exception": false,
     "start_time": "2022-01-23T10:46:16.505019",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(891, 12)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "titanic_train.shape\n",
    "#to briefly see the number of rows and columns in my train dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "a2d0a722",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-23T10:46:16.596831Z",
     "iopub.status.busy": "2022-01-23T10:46:16.589826Z",
     "iopub.status.idle": "2022-01-23T10:46:16.599699Z",
     "shell.execute_reply": "2022-01-23T10:46:16.600160Z",
     "shell.execute_reply.started": "2022-01-23T10:41:54.854204Z"
    },
    "papermill": {
     "duration": 0.03754,
     "end_time": "2022-01-23T10:46:16.600316",
     "exception": false,
     "start_time": "2022-01-23T10:46:16.562776",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    549\n",
       "1    342\n",
       "Name: Survived, dtype: int64"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#i will further get the frquency or count of the survivors to non survivors\n",
    "titanic_train['Survived'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "d6e49d8f",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-23T10:46:16.658012Z",
     "iopub.status.busy": "2022-01-23T10:46:16.657355Z",
     "iopub.status.idle": "2022-01-23T10:46:16.855092Z",
     "shell.execute_reply": "2022-01-23T10:46:16.854619Z",
     "shell.execute_reply.started": "2022-01-23T10:42:03.264208Z"
    },
    "papermill": {
     "duration": 0.227972,
     "end_time": "2022-01-23T10:46:16.855230",
     "exception": false,
     "start_time": "2022-01-23T10:46:16.627258",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Survived', ylabel='count'>"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#i can plot the above outcome using the seaborn library\n",
    "sns.countplot(x = \"Survived\", data = titanic_train)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "198543ca",
   "metadata": {
    "papermill": {
     "duration": 0.02598,
     "end_time": "2022-01-23T10:46:16.907854",
     "exception": false,
     "start_time": "2022-01-23T10:46:16.881874",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**From the above plot, 549 passangers of the train dataset died while 342 passangers survived**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "84fed58e",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-23T10:46:16.963639Z",
     "iopub.status.busy": "2022-01-23T10:46:16.962684Z",
     "iopub.status.idle": "2022-01-23T10:46:16.969551Z",
     "shell.execute_reply": "2022-01-23T10:46:16.970142Z",
     "shell.execute_reply.started": "2022-01-23T10:42:07.823663Z"
    },
    "papermill": {
     "duration": 0.036313,
     "end_time": "2022-01-23T10:46:16.970302",
     "exception": false,
     "start_time": "2022-01-23T10:46:16.933989",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3    491\n",
       "1    216\n",
       "2    184\n",
       "Name: Pclass, dtype: int64"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#similarly, i will determine the number of passangers in each class and also plot my result\n",
    "titanic_train['Pclass'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "0bfd1071",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-23T10:46:17.026134Z",
     "iopub.status.busy": "2022-01-23T10:46:17.025537Z",
     "iopub.status.idle": "2022-01-23T10:46:17.194736Z",
     "shell.execute_reply": "2022-01-23T10:46:17.195209Z",
     "shell.execute_reply.started": "2022-01-23T10:42:13.774052Z"
    },
    "papermill": {
     "duration": 0.198567,
     "end_time": "2022-01-23T10:46:17.195373",
     "exception": false,
     "start_time": "2022-01-23T10:46:16.996806",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Pclass', ylabel='count'>"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(x = \"Pclass\", data = titanic_train)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4b914fbe",
   "metadata": {
    "papermill": {
     "duration": 0.027395,
     "end_time": "2022-01-23T10:46:17.250621",
     "exception": false,
     "start_time": "2022-01-23T10:46:17.223226",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**From the above barplot, we have majority of the passangers(491) in the 3rd class**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "4a0e8d60",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-23T10:46:17.308251Z",
     "iopub.status.busy": "2022-01-23T10:46:17.307657Z",
     "iopub.status.idle": "2022-01-23T10:46:17.313535Z",
     "shell.execute_reply": "2022-01-23T10:46:17.314135Z",
     "shell.execute_reply.started": "2022-01-23T10:42:27.022773Z"
    },
    "papermill": {
     "duration": 0.036523,
     "end_time": "2022-01-23T10:46:17.314290",
     "exception": false,
     "start_time": "2022-01-23T10:46:17.277767",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "male      577\n",
       "female    314\n",
       "Name: Sex, dtype: int64"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Determining the number of males and females in the train dataset\n",
    "titanic_train['Sex'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "5c399873",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-23T10:46:17.372972Z",
     "iopub.status.busy": "2022-01-23T10:46:17.372364Z",
     "iopub.status.idle": "2022-01-23T10:46:17.541617Z",
     "shell.execute_reply": "2022-01-23T10:46:17.542081Z",
     "shell.execute_reply.started": "2022-01-23T10:42:31.654399Z"
    },
    "papermill": {
     "duration": 0.200221,
     "end_time": "2022-01-23T10:46:17.542251",
     "exception": false,
     "start_time": "2022-01-23T10:46:17.342030",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Sex', ylabel='count'>"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(x = \"Sex\", data = titanic_train)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "aa2a33b1",
   "metadata": {
    "papermill": {
     "duration": 0.028334,
     "end_time": "2022-01-23T10:46:17.599806",
     "exception": false,
     "start_time": "2022-01-23T10:46:17.571472",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**We have 577 males and 314 females in the train dataset**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "bccee364",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-23T10:46:17.663655Z",
     "iopub.status.busy": "2022-01-23T10:46:17.659976Z",
     "iopub.status.idle": "2022-01-23T10:46:17.920436Z",
     "shell.execute_reply": "2022-01-23T10:46:17.920930Z",
     "shell.execute_reply.started": "2022-01-23T10:42:52.181723Z"
    },
    "papermill": {
     "duration": 0.292599,
     "end_time": "2022-01-23T10:46:17.921103",
     "exception": false,
     "start_time": "2022-01-23T10:46:17.628504",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Age', ylabel='Count'>"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#To check for the age distribution, i will use a histogram since i am considering the \"Age\" variable which is a continues data\n",
    "sns.histplot(x = \"Age\", data = titanic_train)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c3ebae1f",
   "metadata": {
    "papermill": {
     "duration": 0.029758,
     "end_time": "2022-01-23T10:46:17.980651",
     "exception": false,
     "start_time": "2022-01-23T10:46:17.950893",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**From the above distribution, majority of the passangers are betweent the ages of 20 and 35.**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9ad702a5",
   "metadata": {
    "papermill": {
     "duration": 0.029424,
     "end_time": "2022-01-23T10:46:18.039502",
     "exception": false,
     "start_time": "2022-01-23T10:46:18.010078",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "17394c28",
   "metadata": {
    "papermill": {
     "duration": 0.030033,
     "end_time": "2022-01-23T10:46:18.099635",
     "exception": false,
     "start_time": "2022-01-23T10:46:18.069602",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## Data Wrangling/Cleaning"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "add4e016",
   "metadata": {
    "papermill": {
     "duration": 0.02929,
     "end_time": "2022-01-23T10:46:18.158554",
     "exception": false,
     "start_time": "2022-01-23T10:46:18.129264",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "I will be dropping columns that i believe wouldn't be detaminants of if a passanger survived or not.  \n",
    "the PassangerId, Ticket, Cabin and Name columns will be dropped while the missing values in the age, SibSp, Parch and Fare will be replaced with their respective column averages. The missing values in the \"Embarked\" column will be replaced with \"U\" which stands for unkown. This cleaning will be done on both datasets."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "94e8c88b",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-23T10:46:18.220828Z",
     "iopub.status.busy": "2022-01-23T10:46:18.220208Z",
     "iopub.status.idle": "2022-01-23T10:46:18.230981Z",
     "shell.execute_reply": "2022-01-23T10:46:18.231506Z",
     "shell.execute_reply.started": "2022-01-23T10:43:01.395251Z"
    },
    "papermill": {
     "duration": 0.04352,
     "end_time": "2022-01-23T10:46:18.231668",
     "exception": false,
     "start_time": "2022-01-23T10:46:18.188148",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "#I will create a data cleaning function\n",
    "def clean_data(titanic_train):\n",
    "    titanic_train= titanic_train.drop(['PassengerId', 'Ticket', 'Cabin', 'Name'], axis=1)\n",
    "    \n",
    "    columns = ['SibSp', 'Parch', 'Fare', 'Age']\n",
    "    for col in columns:\n",
    "        titanic_train[col].fillna(titanic_train[col].mean(), inplace=True)\n",
    "    \n",
    "    titanic_train.Embarked.fillna('U', inplace=True)\n",
    "    return titanic_train\n",
    "\n",
    "clean_train = clean_data(titanic_train)\n",
    "clean_test = clean_data(titanic_test)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "371cd6dc",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-23T10:46:18.293505Z",
     "iopub.status.busy": "2022-01-23T10:46:18.292893Z",
     "iopub.status.idle": "2022-01-23T10:46:18.305856Z",
     "shell.execute_reply": "2022-01-23T10:46:18.305275Z",
     "shell.execute_reply.started": "2022-01-23T10:43:16.682616Z"
    },
    "papermill": {
     "duration": 0.044697,
     "end_time": "2022-01-23T10:46:18.306005",
     "exception": false,
     "start_time": "2022-01-23T10:46:18.261308",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Embarked</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>male</td>\n",
       "      <td>22.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>7.2500</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>female</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>female</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>7.9250</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>female</td>\n",
       "      <td>35.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>53.1000</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>male</td>\n",
       "      <td>35.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>8.0500</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Survived  Pclass     Sex   Age  SibSp  Parch     Fare Embarked\n",
       "0         0       3    male  22.0      1      0   7.2500        S\n",
       "1         1       1  female  38.0      1      0  71.2833        C\n",
       "2         1       3  female  26.0      0      0   7.9250        S\n",
       "3         1       1  female  35.0      1      0  53.1000        S\n",
       "4         0       3    male  35.0      0      0   8.0500        S"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "clean_train.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "4604ea53",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-23T10:46:18.371650Z",
     "iopub.status.busy": "2022-01-23T10:46:18.371028Z",
     "iopub.status.idle": "2022-01-23T10:46:18.377165Z",
     "shell.execute_reply": "2022-01-23T10:46:18.377650Z",
     "shell.execute_reply.started": "2022-01-23T10:43:20.512370Z"
    },
    "papermill": {
     "duration": 0.041468,
     "end_time": "2022-01-23T10:46:18.377807",
     "exception": false,
     "start_time": "2022-01-23T10:46:18.336339",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Survived    0\n",
       "Pclass      0\n",
       "Sex         0\n",
       "Age         0\n",
       "SibSp       0\n",
       "Parch       0\n",
       "Fare        0\n",
       "Embarked    0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Checking for null values\n",
    "clean_train.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ad4c5aa1",
   "metadata": {
    "papermill": {
     "duration": 0.030328,
     "end_time": "2022-01-23T10:46:18.438677",
     "exception": false,
     "start_time": "2022-01-23T10:46:18.408349",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**Next, i will need to convert the categorical columns like \"Sex\" and \"Embarked\" into numeric variables by using Sklearn Label Encorder.**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "d1fdefa9",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-23T10:46:18.505997Z",
     "iopub.status.busy": "2022-01-23T10:46:18.502837Z",
     "iopub.status.idle": "2022-01-23T10:46:18.634254Z",
     "shell.execute_reply": "2022-01-23T10:46:18.634835Z",
     "shell.execute_reply.started": "2022-01-23T10:43:26.967226Z"
    },
    "papermill": {
     "duration": 0.165413,
     "end_time": "2022-01-23T10:46:18.635014",
     "exception": false,
     "start_time": "2022-01-23T10:46:18.469601",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['female' 'male']\n",
      "['C' 'Q' 'S' 'U']\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Embarked</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>22.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>7.2500</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>7.9250</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>35.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>53.1000</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>35.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>8.0500</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Survived  Pclass  Sex   Age  SibSp  Parch     Fare  Embarked\n",
       "0         0       3    1  22.0      1      0   7.2500         2\n",
       "1         1       1    0  38.0      1      0  71.2833         0\n",
       "2         1       3    0  26.0      0      0   7.9250         2\n",
       "3         1       1    0  35.0      1      0  53.1000         2\n",
       "4         0       3    1  35.0      0      0   8.0500         2"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn import preprocessing\n",
    "labEn = preprocessing.LabelEncoder()\n",
    "\n",
    "columns = [\"Sex\", \"Embarked\"]\n",
    "\n",
    "for col in columns:\n",
    "    clean_train[col] = labEn.fit_transform(clean_train[col])\n",
    "    clean_test[col] = labEn.transform(clean_test[col])\n",
    "    print(labEn.classes_)\n",
    "    \n",
    "clean_train.head()\n",
    "    \n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ba0fb8a0",
   "metadata": {
    "papermill": {
     "duration": 0.030941,
     "end_time": "2022-01-23T10:46:18.698465",
     "exception": false,
     "start_time": "2022-01-23T10:46:18.667524",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "From the above mapping in \"Sex\" column, \"female\" has be converted to zero and \"male\" is 1. Similarly in the \"Embarked\" column, \"C\" is now zero, \"Q\" is 1, \"S\" is 2 and \"U\" is 3."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e714d3b2",
   "metadata": {
    "papermill": {
     "duration": 0.030727,
     "end_time": "2022-01-23T10:46:18.760334",
     "exception": false,
     "start_time": "2022-01-23T10:46:18.729607",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## Predictive Model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "284b5add",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-23T10:46:18.826329Z",
     "iopub.status.busy": "2022-01-23T10:46:18.825748Z",
     "iopub.status.idle": "2022-01-23T10:46:18.953954Z",
     "shell.execute_reply": "2022-01-23T10:46:18.954520Z",
     "shell.execute_reply.started": "2022-01-23T10:43:36.822781Z"
    },
    "papermill": {
     "duration": 0.163106,
     "end_time": "2022-01-23T10:46:18.954753",
     "exception": false,
     "start_time": "2022-01-23T10:46:18.791647",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.model_selection import train_test_split\n",
    "\n",
    "y=clean_train[\"Survived\"]\n",
    "X=clean_train.drop([\"Survived\"], axis=1)\n",
    "\n",
    "X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.3, random_state=2)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "2311942a",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-23T10:46:19.021401Z",
     "iopub.status.busy": "2022-01-23T10:46:19.020306Z",
     "iopub.status.idle": "2022-01-23T10:46:19.054822Z",
     "shell.execute_reply": "2022-01-23T10:46:19.054141Z",
     "shell.execute_reply.started": "2022-01-23T10:43:40.379246Z"
    },
    "papermill": {
     "duration": 0.068835,
     "end_time": "2022-01-23T10:46:19.054962",
     "exception": false,
     "start_time": "2022-01-23T10:46:18.986127",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "cls = LogisticRegression(random_state=0, max_iter=1000).fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "3f1ea1ef",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-23T10:46:19.121553Z",
     "iopub.status.busy": "2022-01-23T10:46:19.120607Z",
     "iopub.status.idle": "2022-01-23T10:46:19.128804Z",
     "shell.execute_reply": "2022-01-23T10:46:19.129256Z",
     "shell.execute_reply.started": "2022-01-23T10:43:43.984969Z"
    },
    "papermill": {
     "duration": 0.042978,
     "end_time": "2022-01-23T10:46:19.129448",
     "exception": false,
     "start_time": "2022-01-23T10:46:19.086470",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "79%\n"
     ]
    }
   ],
   "source": [
    "predictions = cls.predict(X_val)\n",
    "from sklearn.metrics import accuracy_score\n",
    "acc = accuracy_score(y_val, predictions)*100\n",
    "print(str(round(acc)) + '%')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "890a6e57",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-23T10:46:19.196002Z",
     "iopub.status.busy": "2022-01-23T10:46:19.195132Z",
     "iopub.status.idle": "2022-01-23T10:46:19.203755Z",
     "shell.execute_reply": "2022-01-23T10:46:19.204195Z",
     "shell.execute_reply.started": "2022-01-23T10:43:48.402263Z"
    },
    "papermill": {
     "duration": 0.043378,
     "end_time": "2022-01-23T10:46:19.204357",
     "exception": false,
     "start_time": "2022-01-23T10:46:19.160979",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0,\n",
       "       1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1,\n",
       "       1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1,\n",
       "       1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1,\n",
       "       1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0,\n",
       "       0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0,\n",
       "       1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,\n",
       "       0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1,\n",
       "       1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,\n",
       "       0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0,\n",
       "       1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1,\n",
       "       0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1,\n",
       "       0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0,\n",
       "       0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0,\n",
       "       0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0,\n",
       "       1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0,\n",
       "       0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0,\n",
       "       1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1,\n",
       "       0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0])"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "submission_prediction = cls.predict(clean_test)\n",
    "submission_prediction"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "2ce879fb",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-23T10:46:19.271692Z",
     "iopub.status.busy": "2022-01-23T10:46:19.270758Z",
     "iopub.status.idle": "2022-01-23T10:46:19.275161Z",
     "shell.execute_reply": "2022-01-23T10:46:19.275756Z",
     "shell.execute_reply.started": "2022-01-23T10:43:53.183562Z"
    },
    "papermill": {
     "duration": 0.039793,
     "end_time": "2022-01-23T10:46:19.275916",
     "exception": false,
     "start_time": "2022-01-23T10:46:19.236123",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "#I will now convert the submission into a dataframe.\n",
    "df = pd.DataFrame({\"PassengerId\":test_ids.values,\n",
    "                      \"Survived\":submission_prediction})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "2576a947",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-23T10:46:19.343602Z",
     "iopub.status.busy": "2022-01-23T10:46:19.342626Z",
     "iopub.status.idle": "2022-01-23T10:46:19.349963Z",
     "shell.execute_reply": "2022-01-23T10:46:19.350475Z"
    },
    "papermill": {
     "duration": 0.042823,
     "end_time": "2022-01-23T10:46:19.350649",
     "exception": false,
     "start_time": "2022-01-23T10:46:19.307826",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "df.to_csv(\"titanic_second_submission2.csv\", index = False)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d25d1576",
   "metadata": {
    "papermill": {
     "duration": 0.031934,
     "end_time": "2022-01-23T10:46:19.414920",
     "exception": false,
     "start_time": "2022-01-23T10:46:19.382986",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## My Kaggle submission scored 77% accuracy score as aginst the 79% scored above. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "f755f082",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-23T10:46:19.482233Z",
     "iopub.status.busy": "2022-01-23T10:46:19.481632Z",
     "iopub.status.idle": "2022-01-23T10:46:19.491108Z",
     "shell.execute_reply": "2022-01-23T10:46:19.491607Z",
     "shell.execute_reply.started": "2022-01-23T10:44:07.814052Z"
    },
    "papermill": {
     "duration": 0.04502,
     "end_time": "2022-01-23T10:46:19.491768",
     "exception": false,
     "start_time": "2022-01-23T10:46:19.446748",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>892</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>893</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>894</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>895</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>896</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>413</th>\n",
       "      <td>1305</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>414</th>\n",
       "      <td>1306</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>415</th>\n",
       "      <td>1307</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>416</th>\n",
       "      <td>1308</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>417</th>\n",
       "      <td>1309</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>418 rows × 2 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     PassengerId  Survived\n",
       "0            892         0\n",
       "1            893         0\n",
       "2            894         0\n",
       "3            895         0\n",
       "4            896         1\n",
       "..           ...       ...\n",
       "413         1305         0\n",
       "414         1306         1\n",
       "415         1307         0\n",
       "416         1308         0\n",
       "417         1309         0\n",
       "\n",
       "[418 rows x 2 columns]"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.12"
  },
  "papermill": {
   "default_parameters": {},
   "duration": 14.163917,
   "end_time": "2022-01-23T10:46:20.234313",
   "environment_variables": {},
   "exception": null,
   "input_path": "__notebook__.ipynb",
   "output_path": "__notebook__.ipynb",
   "parameters": {},
   "start_time": "2022-01-23T10:46:06.070396",
   "version": "2.3.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
