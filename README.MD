# Blackjack
---
## Cards

### Data structure

#### Values
| Number | Symbol | Name |
|--- |--- |---    |
| 1  | A  | Ace   |
| 2  | 2  | 2     |
| 3  | 3  | 3     |
| 4  | 4  | 4     |
| 5  | 5  | 5     |
| 6  | 6  | 6     |
| 7  | 7  | 7     |
| 8  | 8  | 8     |
| 9  | 9  | 9     |
| 10 | 10 | 10    |
| 11 | J  | Jack  |
| 12 | Q  | Queen |
| 13 | K  | King  |
| 14 | J  | Joker |

#### Colors
| Number | Symbol | Name |
|---|---|---      |
| 1 | H | Heart   |
| 2 | D | Diamond |
| 3 | C | Club    |
| 4 | S | Spade   |
| 5 | W | White   |
| 6 | B | Black   |
---
#### Naming

##### Short / Debug
> {Values.Symbol}{Colors.Symbol}

##### Short / Debug for Jokers
> {Colors.Symbol}{Values.Symbol}

##### Normal
> {Values.Name} of {Colors.Name}s

##### Normal for Jokers
> {Color.Name} {Values.Name}
---
### Card class
* single card

#### Properites

##### API

* name
  * read only
  * returns full name of the card (for example: "King of Clubs")

* value
  * read only
  * returns value as int
  
* color
  * read only
  * return color as int

* value_name
  * read only
  * returns the name of the card value

* color_name
  * read only
  * returns the name of the card color

* value_symbol
  * read only
  * returns symbol of the card's value

* color_symbol
  * read only
  * returns symbol of the card's color

* symbols
  * read only
  * returns the symbols pair of the card 

##### Helper

* _COLORS
  * classproperty
  * [Number: int, Symbol: str, Name: str]
  
* _VALUES
  * classproperty
  * [Number: int, Symbol: str, Name: str]

* _UNICODE
  * classproperty
  * table with ascii representation for all cards
  * _UNICODE[value - 1][color - 1]
---
#### Methods

##### API

* \_\_init\_\_()
  * creates a Card instance form value and color
  * raises error if inputs are not valid

* \_\_str\_\_()
  * returns full name of the card (same as property "name")

* \_\_eq\_\_()
  * compares 2 cards by thier value and color

* \_\_repr\_\_()
  * returns debug data for card
  * in init format ( for example "Card(value=1, color=1)" )

* from_symbols() 
  * classmethod
  * creates a Card instance from symbols
  * uppercase only
  * raises error if inputs are not valid
  * pass in in natural order

* from_name()
  * classmethod 
  * creates a Card instance from card name
  * raises error for invalid input data
  
##### Helper

* \_find()
  * finds the coresponding value to given value in a table row 

  * inputs
    * table - matrix to search
    * value_to_find - falue that function is looking for
    * watch_column - column that is going to be observed to find the value
    * return_column - column form which the value will return
  
  * output
    * value of any type if value was found
    * None if value was not found