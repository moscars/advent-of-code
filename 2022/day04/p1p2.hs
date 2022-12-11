import Data.Char

strToInt :: String -> Integer
strToInt str = read str :: Integer

getNums :: String -> [Integer]
getNums str = map strToInt (getIntegersStrings str "")

getIntegersStrings :: String -> String -> [String]
getIntegersStrings "" curr = [curr]
getIntegersStrings (x:xs) curr 
    | isDigit x = getIntegersStrings xs (curr ++ [x])
    | otherwise = curr : getIntegersStrings xs ""

splitOnNewLines :: String -> String -> [String]
splitOnNewLines "" curr = [curr]
splitOnNewLines input curr
    | head input == '\n' = [curr] ++ splitOnNewLines (tail input) ""
    | otherwise = splitOnNewLines (tail input) (curr ++ [(head input)])

fullyContains :: [Integer] -> Bool
fullyContains (s1:e1:s2:e2:_)
    | s1 <= s2 && e2 <= e1 = True
    | s2 <= s1 && e1 <= e2 = True
    | otherwise = False

partiallyContains :: [Integer] -> Bool
partiallyContains (s1:e1:s2:e2:_)
    | e1 < s2 = False
    | e2 < s1 = False
    | otherwise = True

countContains :: ([Integer] -> Bool) -> [[Integer]] -> Integer
countContains func [] = 0
countContains func (x:xs)
    | func x = 1 + countContains func xs
    | otherwise = countContains func xs

getOutput :: ([Integer] -> Bool) -> String -> String
getOutput containsFunc input = show $ countContains containsFunc $ map getNums $ splitOnNewLines input ""

main :: IO()
main = do
    lines <- getContents
    putStrLn $ getOutput fullyContains lines
    putStrLn $ getOutput partiallyContains lines