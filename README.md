# ONCT Documentation

The ONCT library provides a collection of modules for retrieving, processing and analysing data in educational contexts.

## Available modules

### onct.data

General data handling functions.

### onct.economie

Functions for retrieving economic data.

Additional modules may be available depending on the installed version of ONCT.

Examples include:

* `onct.biologie`
* `onct.wiskunde`
* `onct.aardrijkskunde`

---

# onct.data — Basic data handling functions

The `onct.data` module provides functions for viewing, storing, loading and converting data.

The functions in this module are independent of any specific data source and may be used together with any ONCT module.

## Functions

### print_json(data, max_characters=4000)

Print data to the terminal in a readable JSON format.

#### Parameters

**data**

Data object to display.

**max_characters**

Maximum number of characters displayed.

#### Returns

```python
None
```

---

### save_json(data, filename)

Save data to a JSON file.

#### Parameters

**data**

Data object to save.

**filename**

Destination filename.

#### Returns

```python
None
```

---

### load_json(filename)

Load data from a JSON file.

#### Parameters

**filename**

Source filename.

#### Returns

```python
dict | list
```

Loaded data object.

---

### json_to_dataframe(

data,
record_path=None,
numeric_columns=None,
datetime_columns=None
)

Convert structured data into a pandas DataFrame.

#### Parameters

**data**

Source data.

**record_path**

Optional key containing records that should become rows in the DataFrame.

**numeric_columns**

Optional list of columns that should be converted to numeric values.

**datetime_columns**

Optional list of columns that should be converted to datetime values.

#### Returns

```python
pandas.DataFrame
```

A pandas DataFrame containing the converted data.

---

# onct.economie — Economic data functions

The `onct.economie` module provides functions for retrieving economic data.

## Functions

### set_stock_api_key(api_key)

Store an API key for accessing stock market data.

#### Parameters

**api_key**

Valid API key.

#### Returns

```python
None
```

---

### get_stock_quote(symbols)

Retrieve quote information for one or more stock symbols.

#### Parameters

**symbols**

Stock symbol or list of stock symbols.

#### Returns

```python
dict
```

Quote data.

---

### get_stock_history(symbols, period="30D")

Retrieve historical stock data.

#### Parameters

**symbols**

Stock symbol or list of stock symbols.

**period**

Requested time period.

Supported values:

```python
"30D"
"100D"
"1Y"
"2Y"
```

#### Returns

```python
dict
```

Historical stock data.

---

# pandas — DataFrame basics

The pandas library provides data structures and functions for data analysis.

The examples below assume a pandas DataFrame stored in the variable `df`.

## Viewing data

### df.head()

Display the first rows of a DataFrame.

#### Returns

```python
pandas.DataFrame
```

#### Example

```python
df.head()
```

---

### df.columns

Display the column names of a DataFrame.

#### Returns

```python
pandas.Index
```

#### Example

```python
df.columns
```

---

### df.describe()

Generate descriptive statistics for numeric columns.

#### Returns

```python
pandas.DataFrame
```

#### Example

```python
df.describe()
```

---

## Selecting data

### df["column_name"]

Select a column from a DataFrame.

#### Parameters

**column_name**

Name of the column.

#### Returns

```python
pandas.Series
```

#### Example

```python
df["column_name"]
```

---

## Statistical functions

### df["column_name"].mean()

Calculate the average value of a column.

#### Returns

```python
float
```

#### Example

```python
df["column_name"].mean()
```

---

### df["column_name"].max()

Return the highest value in a column.

#### Returns

```python
float
```

#### Example

```python
df["column_name"].max()
```

---

### df["column_name"].min()

Return the lowest value in a column.

#### Returns

```python
float
```

#### Example

```python
df["column_name"].min()
```

---

## Visualisation

### df["column_name"].plot()

Create a graph from a column.

#### Returns

```python
matplotlib.axes.Axes
```

#### Example

```python
df["column_name"].plot()
```
