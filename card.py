from typing import Any


class Card:
    #! CONSTANTS

    _UNICODE: list[list[str | None]] = [
        #? 1    2     3    4     5     6
        ['🂱', '🃁', '🃑', '🂡', None, None],  #? 1
        ['🂲', '🃂', '🃒', '🂢', None, None],  #? 2
        ['🂳', '🃃', '🃓', '🂣', None, None],  #? 3
        ['🂴', '🃄', '🃔', '🂤', None, None],  #? 4
        ['🂵', '🃅', '🃕', '🂥', None, None],  #? 5
        ['🂶', '🃆', '🃖', '🂦', None, None],  #? 6
        ['🂷', '🃇', '🃗', '🂧', None, None],  #? 7
        ['🂸', '🃈', '🃘', '🂨', None, None],  #? 8
        ['🂹', '🃉', '🃙', '🂩', None, None],  #? 9
        ['🂺', '🃊', '🃚', '🂪', None, None],  #? 10
        ['🂻', '🃋', '🃛', '🂫', None, None],  #? 11
        ['🂽', '🃍', '🃝', '🂭', None, None],  #? 12
        ['🂾', '🃎', '🃞', '🂮', None, None],  #? 13
        [None, None, None, None, '🃟', '🃏'], #? 14
    ]
    
    #? [Number: int, Symbol: str, Name: str]
    _COLORS: list[list[str | int]] = [
        [1, "H", "Heart"   ],
        [2, "D", "Diamond" ],
        [3, "C", "Club"    ],
        [4, "S", "Spade"   ],
        [5, "W", "White"   ],
        [6, "B", "Black"   ],
    ]

    #? [Number: int, Symbol: str, Name: str]
    _VALUES: list[list[str | int]] = [
        [1,  "A",  "Ace"   ],
        [2,  "2",  "2"     ],
        [3,  "3",  "3"     ],
        [4,  "4",  "4"     ],
        [5,  "5",  "5"     ],
        [6,  "6",  "6"     ],
        [7,  "7",  "7"     ],
        [8,  "8",  "8"     ],
        [9,  "9",  "9"     ],
        [10, "10", "10"    ],
        [11, "J",  "Jack"  ],
        [12, "Q",  "Queen" ],
        [13, "K",  "King"  ],
        [14, "J",  "Joker" ],
    ]

    #! DUNDER METHODS

    def __init__(self, *, value: int, color: int) -> None:
        assert value >= 1 and value <= 14, f"Value not in range of values [1, 14]\n\
            value=>{value}<=value"
        assert color >= 1 and color <= 6, f"Color not in range of color [1, 6]\n\
            color=>{color}<=color"
    
        if value == 14:
            assert color == 5 or color == 6, f"Jokers can have only color 5 or color 6\n\
                color=>{color}<=color"
        else:
            assert color != 5 and color != 6, f"Only jokers can have color 5 or color 6\n\
                color=>{color}<=color"

        self._value: int = value
        self._color: int = color

        self._value_name: str | None = self._find(
            table=self._VALUES,
            value_to_find=self._value,
            watch_column=0,
            return_column=2
        )

        self._color_name: str | None = self._find(
            table=self._COLORS,
            value_to_find=self._color,
            watch_column=0,
            return_column=2
        )

        assert self._value_name != None, f"value_number not found for\n\
                value_name=>{self._value_name}<=value_name"
        assert self._color_name != None, f"color_name not found for\n\
            color_name=>{self._color_name}<=color_name"
        

        self._value_symbol: str | None = self._find(
            table=self._VALUES,
            value_to_find=self._value,
            watch_column=0,
            return_column=1,
        )

        self._color_symbol: str | None = self._find(
            table=self._COLORS,
            value_to_find=self._color,
            watch_column=0,
            return_column=1,
        )

        assert self._value_symbol != None, f"value_symbol not found for\n\
            value_symbol=>{self._value_symbol}<=value_symbol"
        assert self._color_symbol != None, f"color_symbol not found for\n\
            color_symbol=>{self._color_symbol}<=color_symbol"

        


        
        if self._value == 14:
            self._name = f"{self._color_name} {self._value_name}"
            self._symbols = f"{self._color_symbol}{self._value_symbol}"
        
        else:
            self._name = f"{self._value_name} of {self._color_name}s"
            self._symbols = f"{self._value_symbol}{self._color_symbol}"

        self._unicode: str | None = self._UNICODE[value - 1][color - 1]
        
        assert self._unicode != None, f"Coresponding unicode not found for\n\
            value={self._value}\ncolor={self._color}"

    def __str__(self) -> str:
        return self._name
    
    def __eq__(self, other: "Card") -> bool:
        return self.value == other.value and self.color == other.color

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(value={self._value}, color={self._color})"

    #! PROPERTIES

    @property
    def name(self) -> str:
        return self._name

    @property
    def value(self) -> int:
        return self._value
    
    @property
    def color(self) -> int:
        return self._color
    
    @property
    def unicode(self) -> str:
        return self._unicode   #type: ignore # it's not possibe to return None
    
    @property
    def value_name(self) -> str:
        return self._value_name   #type: ignore # it's not possibe to return None
    
    @property
    def color_name(self) -> str:
        return self._color_name   #type: ignore # it's not possibe to return None
    
    @property
    def value_symbol(self) -> str:
        return self._value_symbol   #type: ignore # it's not possibe to return None
    
    @property
    def color_symbol(self) -> str:
        return self._color_symbol   #type: ignore # it's not possibe to return None

    @property
    def symbols(self) -> str:
        return self._symbols    
    
    @property
    def is_joker(self) -> bool:
        return self._value == 14

    @property
    def number(self) -> int:
        return 0    #todo            init too


    #! CLASSMETHODS

    @classmethod
    def from_symbols(cls, symbol1: str, symbol2 :str) -> "Card":
        if symbol2 == "J":
            if symbol1 == "W":
                return cls(value=14, color=5)
            elif symbol1 == "B":
                return cls(value=14, color=6)
        else:
            value: int | None = cls._find(
                table=cls._VALUES,
                watch_column=1,
                return_column=0,
                value_to_find=symbol1,
            )

            color: int | None = cls._find(
                table=cls._COLORS,
                watch_column=1,
                return_column=0,
                value_to_find=symbol2,
            )
            
            assert value != None, f"Value number not found for\n\
                symbol1=>{symbol1}<=symbol1"
            assert color != None, f"Color number not found for\n\
                symbol2=>{symbol2}<=symbol2"
            
            return cls(value=value, color=color)   #type: ignore # None raises en error
        
        raise Exception(f"Invaid card symbols\n\
                        symbol1=>{symbol1}<=symbol1\n\
                        symbol2=>{symbol2}<=symbol2")
                


    @classmethod
    def from_name(cls, name: str) -> "Card":
        assert name == name.strip(), f"Invalid card name (try removing wihtespaces)\n\
            card name=>{name}<=card name"

        try:
            if name == "White Joker":
                return cls(value=14, color=5)
            if name == "Black Joker":
                return cls(value=14, color=5)
            
            words = name.split(' ')
            value_name = words[0]
            color_name = words[2][:-1] 

            assert len(words) == 3, f"Too many words ({len(words)})\n\
                words=>{words}<=words"

            value_number: int | None = cls._find(
                table=cls._VALUES,
                value_to_find=value_name,
                watch_column=2,
                return_column=0,
            )

            color_number: int | None = cls._find(
                table=cls._COLORS,
                value_to_find=color_name,
                watch_column=2,
                return_column=0,
            )

            assert value_number != None, f"value_number not found\n\
                value_number=>{value_number}<=value_number"
            assert color_number != None, f"color_number not found\n\
                color_number=>{color_number}<=color_number"
            

            return cls(value=value_number, color=color_number)   #type: ignore # None raises an error
        
        except IndexError:
            assert False, f"Invalid card name\n\
                card name=>{name}<=card name"
            
    @classmethod
    def from_number(cls, number: int) -> "Card":
        assert 1 <= number and number <= 54, f"Invalid number\n\
            number=>{number}<=number"
        
        if number == 53:
            return cls(value=14, color=5)
        elif number == 54:
            return cls(value=14, color=6)
        else:
            color, value  = divmod(number-1, 13)
            return cls(value=value+1, color=color+1)


    #! HELPER METHODS

    @staticmethod
    def _find(
            *,
            table:list[list[Any]],
            watch_column: int,
            value_to_find: Any,
            return_column: int
            ) -> Any | None:
        
        assert len(table) > 0, "The table is empty"

        assert watch_column >= 0, f"watch_column can't be negative! watch_column={watch_column}"
        assert watch_column < len(table[0]),\
            f"watch_column is too big\n \
        Table has only {len(table[0])} columns, not {watch_column} columns"
        
        assert return_column >= 0, f"return_column can't be negative! return_column={return_column}"
        assert return_column < len(table[0]),\
            f"return_column is too big\n \
            Table has only {len(table[0])} columns, not {return_column} columns"
        

        for row in table:
            if row[watch_column] == value_to_find:
                return row[return_column]
        
        return None



