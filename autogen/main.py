from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

def generate(prompt):
  response = client.chat.completions.create(
    model="gpt-3.5-turbo-16k",
    messages=[
      {
        "role": "system",
        "content": "You are an experienced python program with expertise in writing property-based tests using Hypothesis, a python library for this. To use hypothesis, we need to write a strategy using the strategies module in hypothesis, and then provide these in the @given decorator on the test function. You will be provided a function signature and docstring and you will be asked to provide a strategy for testing with Hypothesis. You MUST end by creating a variable called 'strategy' which contains the strategies you create. Do NOT include any tests in your responses."
      },
      {
        "role": "user",
        "content": "def has_close_elements(numbers: List[float], threshold: float) -> bool:\n    \"\"\" Check if in given list of numbers, are any two numbers closer to each other than\n    given threshold.\n    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)\n    False\n    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)\n    True\n    \"\"\""
      },
      {
        "role": "assistant",
        "content": "numbers = lists(one_of(integers(), floats()), max_size=MAX_SEQUENCE_LEN)\nthreshold = floats(min_value=0.0, exclude_min=True)\n\nstrategy = numbers, threshold"
      },
      {
        "role": "user",
        "content": "def parse_nested_parens(paren_string: str) -> List[int]:\n    \"\"\" Input to this function is a string represented multiple groups for nested parentheses separated by spaces.\n    For each of the group, output the deepest level of nesting of parentheses.\n    E.g. (()()) has maximum two levels of nesting while ((())) has three.\n\n    >>> parse_nested_parens('(()()) ((())) () ((())()())')\n    [2, 3, 1, 3]\n    \"\"\""
      },
      {
        "role": "assistant",
        "content": "def paren_helper():\n    base = just(' ') | just('')\n    return recursive(base, lists)\n\ndef to_paren(s):\n    s = ''.join(str(x) for x in s)\n    s = s.replace('[', '(').replace(']', ')').replace(',', '').replace(\"'\", '')\n    return s\n\ndef paren_string():\n    return paren_helper().map(to_paren)\n\nstrategy = paren_string()"
      },
      {
        "role": "user",
        "content": "def string_xor(a: str, b: str) -> str:\n    \"\"\" Input are two strings a and b consisting only of 1s and 0s.\n    Perform binary XOR on these inputs and return result also as a string.\n    >>> string_xor('010', '110')\n    '100'\n    \"\"\""
      },
      {
        "role": "assistant",
        "content": "@composite\ndef make(draw):\n    n = draw(integers(min_value=1, max_value=MAX_SEQUENCE_LEN))\n    a = draw(text(alphabet='01', min_size=n, max_size=n))\n    b = draw(text(alphabet='01', min_size=n, max_size=n))\n    return a, b\n\nv = make()\na = shared(v, key='eval').map(lambda x: x[0])\nb = shared(v, key='eval').map(lambda x: x[1])\n\nstrategy = a, b"
      },
      {
        "role": "user",
        "content": "def remove_duplicates(numbers: List[int]) -> List[int]:\n    \"\"\" From a list of integers, remove all elements that occur more than once.\n    Keep order of elements left the same as in the input.\n    >>> remove_duplicates([1, 2, 3, 2, 4])\n    [1, 3, 4]\n    \"\"\""
      },
      {
        "role": "assistant",
        "content": "numbers = lists(integers(min_value=MIN_INT, max_value=MAX_INT), max_size=MAX_SEQUENCE_LEN)\n\nstrategy = numbers"
      },
      {
        "role": "user",
        "content": "def max_fill(grid, capacity):\n    \"\"\"\n    You are given a rectangular grid of wells. Each row represents a single well,\n    and each 1 in a row represents a single unit of water.\n    Each well has a corresponding bucket that can be used to extract water from it, \n    and all buckets have the same capacity.\n    Your task is to use the buckets to empty the wells.\n    Output the number of times you need to lower the buckets.\n\n    Example 1:\n        Input: \n            grid : [[0,0,1,0], [0,1,0,0], [1,1,1,1]]\n            bucket_capacity : 1\n        Output: 6\n\n    Example 2:\n        Input: \n            grid : [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]\n            bucket_capacity : 2\n        Output: 5\n    \n    Example 3:\n        Input: \n            grid : [[0,0,0], [0,0,0]]\n            bucket_capacity : 5\n        Output: 0\n\n    Constraints:\n        * all wells have the same length\n        * 1 <= grid.length <= 10^2\n        * 1 <= grid[:,1].length <= 10^2\n        * grid[i][j] -> 0 | 1\n        * 1 <= capacity <= 10\n    \"\"\""
      },
      {
        "role": "assistant",
        "content": "@composite\ndef create_grid(draw):\n    n = draw(integers(min_value=1, max_value=100))\n    grid = draw(lists(lists(integers(min_value=0, max_value=1), min_size=n, max_size=n), min_size=n, max_size=n))\n    return grid\n\ngrid = create_grid()\ncapacity = integers(min_value=1, max_value=10)\n\nstrategy = grid, capacity"
      },
      {
        "role": "user",
        "content": prompt
      }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )  

  return [part.message.content for part in response.choices]
