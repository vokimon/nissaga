# KinFile

- [1. [Optional] Property styles](#styles)
- [2. [Optional] Property families](#families)
  - [2.1. Family](#families_items)
    - [2.1.1. [Optional] Property parents](#families_items_parents)
      - [2.1.1.1. items](#families_items_parents_items)
        - [2.1.1.1.1. Property `item 0`](#families_items_parents_items_anyOf_i0)
        - [2.1.1.1.2. Property `item 1`](#families_items_parents_items_anyOf_i1)
          - [2.1.1.1.2.1. [Optional] Property Person](#families_items_parents_items_anyOf_i1_additionalProperties)
    - [2.1.2. [Optional] Property children](#families_items_children)
      - [2.1.2.1. items](#families_items_children_items)
        - [2.1.2.1.1. Property `item 0`](#families_items_children_items_anyOf_i0)
        - [2.1.2.1.2. Property `item 1`](#families_items_children_items_anyOf_i1)
          - [2.1.2.1.2.1. [Optional] Property Person](#families_items_children_items_anyOf_i1_additionalProperties)
    - [2.1.3. [Optional] Property married](#families_items_married)
      - [2.1.3.1. Property `item 0`](#families_items_married_anyOf_i0)
      - [2.1.3.2. Property `item 1`](#families_items_married_anyOf_i1)
      - [2.1.3.3. Property `item 2`](#families_items_married_anyOf_i2)
      - [2.1.3.4. Property `item 3`](#families_items_married_anyOf_i3)
    - [2.1.4. [Optional] Property divorced](#families_items_divorced)
      - [2.1.4.1. Property `item 0`](#families_items_divorced_anyOf_i0)
      - [2.1.4.2. Property `item 1`](#families_items_divorced_anyOf_i1)
      - [2.1.4.3. Property `item 2`](#families_items_divorced_anyOf_i2)
      - [2.1.4.4. Property `item 3`](#families_items_divorced_anyOf_i3)
    - [2.1.5. [Optional] Property house](#families_items_house)
    - [2.1.6. [Optional] Property notes](#families_items_notes)
    - [2.1.7. [Optional] Property docs](#families_items_docs)
      - [2.1.7.1. items](#families_items_docs_items)
    - [2.1.8. [Optional] Property families](#families_items_families)
      - [2.1.8.1. Family](#families_items_families_items)
- [3. [Optional] Property people](#people)
  - [3.1. [Optional] Property Person](#people_additionalProperties)
    - [3.1.1. [Optional] Property fullname](#families_items_parents_items_anyOf_i1_additionalProperties_fullname)
    - [3.1.2. [Optional] Property name](#families_items_parents_items_anyOf_i1_additionalProperties_name)
    - [3.1.3. [Optional] Property born](#families_items_parents_items_anyOf_i1_additionalProperties_born)
      - [3.1.3.1. Property `item 0`](#families_items_parents_items_anyOf_i1_additionalProperties_born_anyOf_i0)
      - [3.1.3.2. Property `item 1`](#families_items_parents_items_anyOf_i1_additionalProperties_born_anyOf_i1)
      - [3.1.3.3. Property `item 2`](#families_items_parents_items_anyOf_i1_additionalProperties_born_anyOf_i2)
      - [3.1.3.4. Property `item 3`](#families_items_parents_items_anyOf_i1_additionalProperties_born_anyOf_i3)
    - [3.1.4. [Optional] Property died](#families_items_parents_items_anyOf_i1_additionalProperties_died)
      - [3.1.4.1. Property `item 0`](#families_items_parents_items_anyOf_i1_additionalProperties_died_anyOf_i0)
      - [3.1.4.2. Property `item 1`](#families_items_parents_items_anyOf_i1_additionalProperties_died_anyOf_i1)
      - [3.1.4.3. Property `item 2`](#families_items_parents_items_anyOf_i1_additionalProperties_died_anyOf_i2)
      - [3.1.4.4. Property `item 3`](#families_items_parents_items_anyOf_i1_additionalProperties_died_anyOf_i3)
    - [3.1.5. [Optional] Property age](#families_items_parents_items_anyOf_i1_additionalProperties_age)
    - [3.1.6. [Optional] Property comment](#families_items_parents_items_anyOf_i1_additionalProperties_comment)
      - [3.1.6.1. Property `item 0`](#families_items_parents_items_anyOf_i1_additionalProperties_comment_anyOf_i0)
      - [3.1.6.2. Property `item 1`](#families_items_parents_items_anyOf_i1_additionalProperties_comment_anyOf_i1)
        - [3.1.6.2.1. items](#families_items_parents_items_anyOf_i1_additionalProperties_comment_anyOf_i1_items)
    - [3.1.7. [Optional] Property notes](#families_items_parents_items_anyOf_i1_additionalProperties_notes)
      - [3.1.7.1. Property `item 0`](#families_items_parents_items_anyOf_i1_additionalProperties_notes_anyOf_i0)
      - [3.1.7.2. Property `item 1`](#families_items_parents_items_anyOf_i1_additionalProperties_notes_anyOf_i1)
        - [3.1.7.2.1. items](#families_items_parents_items_anyOf_i1_additionalProperties_notes_anyOf_i1_items)
    - [3.1.8. [Optional] Property alias](#families_items_parents_items_anyOf_i1_additionalProperties_alias)
    - [3.1.9. [Optional] Property from](#families_items_parents_items_anyOf_i1_additionalProperties_from)
    - [3.1.10. [Optional] Property todo](#families_items_parents_items_anyOf_i1_additionalProperties_todo)
      - [3.1.10.1. Property `item 0`](#families_items_parents_items_anyOf_i1_additionalProperties_todo_anyOf_i0)
      - [3.1.10.2. Property `item 1`](#families_items_parents_items_anyOf_i1_additionalProperties_todo_anyOf_i1)
        - [3.1.10.2.1. items](#families_items_parents_items_anyOf_i1_additionalProperties_todo_anyOf_i1_items)
    - [3.1.11. [Optional] Property pics](#families_items_parents_items_anyOf_i1_additionalProperties_pics)
      - [3.1.11.1. items](#families_items_parents_items_anyOf_i1_additionalProperties_pics_items)
    - [3.1.12. [Optional] Property docs](#families_items_parents_items_anyOf_i1_additionalProperties_docs)
      - [3.1.12.1. items](#families_items_parents_items_anyOf_i1_additionalProperties_docs_items)
    - [3.1.13. [Optional] Property links](#families_items_parents_items_anyOf_i1_additionalProperties_links)
      - [3.1.13.1. items](#families_items_parents_items_anyOf_i1_additionalProperties_links_items)
    - [3.1.14. [Optional] Property gender](#families_items_parents_items_anyOf_i1_additionalProperties_gender)
    - [3.1.15. [Optional] Property class](#families_items_parents_items_anyOf_i1_additionalProperties_class)
      - [3.1.15.1. items](#families_items_parents_items_anyOf_i1_additionalProperties_class_items)

**Title:** KinFile

| Type                      | `object`                                                |
| ------------------------- | ------------------------------------------------------- |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |
|                           |                                                         |

**Description:** Top level element containing the data required to build a family tree

<details>
<summary><strong> <a name="styles"></a>1. [Optional] Property styles</strong>  

</summary>
<blockquote>

**Title:** Styles

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
</details>

<details>
<summary><strong> <a name="families"></a>2. [Optional] Property families</strong>  

</summary>
<blockquote>

**Title:** Families

| Type                      | `array`                                                                   |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |
|                      |                    |

| Each item of this array must be | Description                                                                    |
| ------------------------------- | ------------------------------------------------------------------------------ |
| [Family](#families_items)       | Represents a family kernel with parents and children and any descendant family |
|                                 |                                                                                |

### <a name="families_items"></a>2.1. Family

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/Family                                                      |
|                           |                                                                           |

**Description:** Represents a family kernel with parents and children and any descendant family

<details>
<summary><strong> <a name="families_items_parents"></a>2.1.1. [Optional] Property parents</strong>  

</summary>
<blockquote>

**Title:** Parents

| Type                      | `array`                                                                   |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |
|                      |                    |

| Each item of this array must be        | Description |
| -------------------------------------- | ----------- |
| [items](#families_items_parents_items) | -           |
|                                        |             |

##### <a name="families_items_parents_items"></a>2.1.1.1. items

| Type                      | `combining`                                                               |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

<blockquote>

| Any of(Option)                                   |
| ------------------------------------------------ |
| [item 0](#families_items_parents_items_anyOf_i0) |
| [item 1](#families_items_parents_items_anyOf_i1) |
|                                                  |

<blockquote>

##### <a name="families_items_parents_items_anyOf_i0"></a>2.1.1.1.1. Property `item 0`

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
<blockquote>

##### <a name="families_items_parents_items_anyOf_i1"></a>2.1.1.1.2. Property `item 1`

| Type                      | `object`                                                                                                                                        |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [[Should-conform]](#families_items_parents_items_anyOf_i1_additionalProperties "Each additional property must conform to the following schema") |
|                           |                                                                                                                                                 |

<details>
<summary><strong> <a name="families_items_parents_items_anyOf_i1_additionalProperties"></a>2.1.1.1.2.1. [Optional] Property Person</strong>  

</summary>
<blockquote>

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Same definition as**    | [Person](#people_additionalProperties)                                    |
|                           |                                                                           |

**Description:** Represents the data of a person

</blockquote>
</details>

</blockquote>

</blockquote>

</blockquote>
</details>

<details>
<summary><strong> <a name="families_items_children"></a>2.1.2. [Optional] Property children</strong>  

</summary>
<blockquote>

**Title:** Children

| Type                      | `array`                                                                   |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |
|                      |                    |

| Each item of this array must be         | Description |
| --------------------------------------- | ----------- |
| [items](#families_items_children_items) | -           |
|                                         |             |

##### <a name="families_items_children_items"></a>2.1.2.1. items

| Type                      | `combining`                                                               |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

<blockquote>

| Any of(Option)                                    |
| ------------------------------------------------- |
| [item 0](#families_items_children_items_anyOf_i0) |
| [item 1](#families_items_children_items_anyOf_i1) |
|                                                   |

<blockquote>

##### <a name="families_items_children_items_anyOf_i0"></a>2.1.2.1.1. Property `item 0`

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
<blockquote>

##### <a name="families_items_children_items_anyOf_i1"></a>2.1.2.1.2. Property `item 1`

| Type                      | `object`                                                                                                                                         |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Additional properties** | [[Should-conform]](#families_items_children_items_anyOf_i1_additionalProperties "Each additional property must conform to the following schema") |
|                           |                                                                                                                                                  |

<details>
<summary><strong> <a name="families_items_children_items_anyOf_i1_additionalProperties"></a>2.1.2.1.2.1. [Optional] Property Person</strong>  

</summary>
<blockquote>

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Same definition as**    | [Person](#families_items_parents_items_anyOf_i1_additionalProperties)     |
|                           |                                                                           |

**Description:** Represents the data of a person

</blockquote>
</details>

</blockquote>

</blockquote>

</blockquote>
</details>

<details>
<summary><strong> <a name="families_items_married"></a>2.1.3. [Optional] Property married</strong>  

</summary>
<blockquote>

**Title:** Married

| Type                      | `combining`                                                               |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `true`                                                                    |
|                           |                                                                           |

<blockquote>

| Any of(Option)                             |
| ------------------------------------------ |
| [item 0](#families_items_married_anyOf_i0) |
| [item 1](#families_items_married_anyOf_i1) |
| [item 2](#families_items_married_anyOf_i2) |
| [item 3](#families_items_married_anyOf_i3) |
|                                            |

<blockquote>

##### <a name="families_items_married_anyOf_i0"></a>2.1.3.1. Property `item 0`

| Type                      | `boolean`                                                                 |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
<blockquote>

##### <a name="families_items_married_anyOf_i1"></a>2.1.3.2. Property `item 1`

| Type                      | `integer`                                                                 |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
<blockquote>

##### <a name="families_items_married_anyOf_i2"></a>2.1.3.3. Property `item 2`

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
<blockquote>

##### <a name="families_items_married_anyOf_i3"></a>2.1.3.4. Property `item 3`

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>

</blockquote>

</blockquote>
</details>

<details>
<summary><strong> <a name="families_items_divorced"></a>2.1.4. [Optional] Property divorced</strong>  

</summary>
<blockquote>

**Title:** Divorced

| Type                      | `combining`                                                               |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `false`                                                                   |
|                           |                                                                           |

<blockquote>

| Any of(Option)                              |
| ------------------------------------------- |
| [item 0](#families_items_divorced_anyOf_i0) |
| [item 1](#families_items_divorced_anyOf_i1) |
| [item 2](#families_items_divorced_anyOf_i2) |
| [item 3](#families_items_divorced_anyOf_i3) |
|                                             |

<blockquote>

##### <a name="families_items_divorced_anyOf_i0"></a>2.1.4.1. Property `item 0`

| Type                      | `boolean`                                                                 |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
<blockquote>

##### <a name="families_items_divorced_anyOf_i1"></a>2.1.4.2. Property `item 1`

| Type                      | `integer`                                                                 |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
<blockquote>

##### <a name="families_items_divorced_anyOf_i2"></a>2.1.4.3. Property `item 2`

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
<blockquote>

##### <a name="families_items_divorced_anyOf_i3"></a>2.1.4.4. Property `item 3`

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>

</blockquote>

</blockquote>
</details>

<details>
<summary><strong> <a name="families_items_house"></a>2.1.5. [Optional] Property house</strong>  

</summary>
<blockquote>

**Title:** House

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
</details>

<details>
<summary><strong> <a name="families_items_notes"></a>2.1.6. [Optional] Property notes</strong>  

</summary>
<blockquote>

**Title:** Notes

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
</details>

<details>
<summary><strong> <a name="families_items_docs"></a>2.1.7. [Optional] Property docs</strong>  

</summary>
<blockquote>

**Title:** Docs

| Type                      | `array of string`                                                         |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |
|                      |                    |

| Each item of this array must be     | Description |
| ----------------------------------- | ----------- |
| [items](#families_items_docs_items) | -           |
|                                     |             |

##### <a name="families_items_docs_items"></a>2.1.7.1. items

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
</details>

<details>
<summary><strong> <a name="families_items_families"></a>2.1.8. [Optional] Property families</strong>  

</summary>
<blockquote>

**Title:** Families

| Type                      | `array`                                                                   |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `[]`                                                                      |
|                           |                                                                           |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |
|                      |                    |

| Each item of this array must be          | Description                                                                    |
| ---------------------------------------- | ------------------------------------------------------------------------------ |
| [Family](#families_items_families_items) | Represents a family kernel with parents and children and any descendant family |
|                                          |                                                                                |

##### <a name="families_items_families_items"></a>2.1.8.1. Family

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Same definition as**    | [Family](#families_items)                                                 |
|                           |                                                                           |

**Description:** Represents a family kernel with parents and children and any descendant family

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary><strong> <a name="people"></a>3. [Optional] Property people</strong>  

</summary>
<blockquote>

**Title:** People

| Type                      | `object`                                                                                                         |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [[Should-conform]](#people_additionalProperties "Each additional property must conform to the following schema") |
| **Default**               | `{}`                                                                                                             |
|                           |                                                                                                                  |

<details>
<summary><strong> <a name="people_additionalProperties"></a>3.1. [Optional] Property Person</strong>  

</summary>
<blockquote>

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/Person                                                      |
|                           |                                                                           |

**Description:** Represents the data of a person

<details>
<summary><strong> <a name="families_items_parents_items_anyOf_i1_additionalProperties_fullname"></a>3.1.1. [Optional] Property fullname</strong>  

</summary>
<blockquote>

**Title:** Fullname

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

**Description:** Surnames are placed first, followed by a comma and then the first name. If no comma, it is just considered the first name

</blockquote>
</details>

<details>
<summary><strong> <a name="families_items_parents_items_anyOf_i1_additionalProperties_name"></a>3.1.2. [Optional] Property name</strong>  

</summary>
<blockquote>

**Title:** Name

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

**Description:** TODO: Explain difference between id, name, fullname and alias. or a year or a string annotation.

</blockquote>
</details>

<details>
<summary><strong> <a name="families_items_parents_items_anyOf_i1_additionalProperties_born"></a>3.1.3. [Optional] Property born</strong>  

</summary>
<blockquote>

**Title:** Born

| Type                      | `combining`                                                               |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `true`                                                                    |
|                           |                                                                           |

**Description:** Date of birth or false to indicate stillborn, or true to indicate unknown date or a year or a string annotation.

<blockquote>

| Any of(Option)                                                                      |
| ----------------------------------------------------------------------------------- |
| [item 0](#families_items_parents_items_anyOf_i1_additionalProperties_born_anyOf_i0) |
| [item 1](#families_items_parents_items_anyOf_i1_additionalProperties_born_anyOf_i1) |
| [item 2](#families_items_parents_items_anyOf_i1_additionalProperties_born_anyOf_i2) |
| [item 3](#families_items_parents_items_anyOf_i1_additionalProperties_born_anyOf_i3) |
|                                                                                     |

<blockquote>

##### <a name="families_items_parents_items_anyOf_i1_additionalProperties_born_anyOf_i0"></a>3.1.3.1. Property `item 0`

| Type                      | `boolean`                                                                 |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
<blockquote>

##### <a name="families_items_parents_items_anyOf_i1_additionalProperties_born_anyOf_i1"></a>3.1.3.2. Property `item 1`

| Type                      | `integer`                                                                 |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
<blockquote>

##### <a name="families_items_parents_items_anyOf_i1_additionalProperties_born_anyOf_i2"></a>3.1.3.3. Property `item 2`

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
<blockquote>

##### <a name="families_items_parents_items_anyOf_i1_additionalProperties_born_anyOf_i3"></a>3.1.3.4. Property `item 3`

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>

</blockquote>

</blockquote>
</details>

<details>
<summary><strong> <a name="families_items_parents_items_anyOf_i1_additionalProperties_died"></a>3.1.4. [Optional] Property died</strong>  

</summary>
<blockquote>

**Title:** Died

| Type                      | `combining`                                                               |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `false`                                                                   |
|                           |                                                                           |

**Description:** Date of death of true to indicate dead but unknown date or a year or a string annotation.

<blockquote>

| Any of(Option)                                                                      |
| ----------------------------------------------------------------------------------- |
| [item 0](#families_items_parents_items_anyOf_i1_additionalProperties_died_anyOf_i0) |
| [item 1](#families_items_parents_items_anyOf_i1_additionalProperties_died_anyOf_i1) |
| [item 2](#families_items_parents_items_anyOf_i1_additionalProperties_died_anyOf_i2) |
| [item 3](#families_items_parents_items_anyOf_i1_additionalProperties_died_anyOf_i3) |
|                                                                                     |

<blockquote>

##### <a name="families_items_parents_items_anyOf_i1_additionalProperties_died_anyOf_i0"></a>3.1.4.1. Property `item 0`

| Type                      | `boolean`                                                                 |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
<blockquote>

##### <a name="families_items_parents_items_anyOf_i1_additionalProperties_died_anyOf_i1"></a>3.1.4.2. Property `item 1`

| Type                      | `integer`                                                                 |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
<blockquote>

##### <a name="families_items_parents_items_anyOf_i1_additionalProperties_died_anyOf_i2"></a>3.1.4.3. Property `item 2`

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
<blockquote>

##### <a name="families_items_parents_items_anyOf_i1_additionalProperties_died_anyOf_i3"></a>3.1.4.4. Property `item 3`

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>

</blockquote>

</blockquote>
</details>

<details>
<summary><strong> <a name="families_items_parents_items_anyOf_i1_additionalProperties_age"></a>3.1.5. [Optional] Property age</strong>  

</summary>
<blockquote>

**Title:** Age

| Type                      | `integer`                                                                 |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
</details>

<details>
<summary><strong> <a name="families_items_parents_items_anyOf_i1_additionalProperties_comment"></a>3.1.6. [Optional] Property comment</strong>  

</summary>
<blockquote>

**Title:** Comment

| Type                      | `combining`                                                               |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

<blockquote>

| Any of(Option)                                                                         |
| -------------------------------------------------------------------------------------- |
| [item 0](#families_items_parents_items_anyOf_i1_additionalProperties_comment_anyOf_i0) |
| [item 1](#families_items_parents_items_anyOf_i1_additionalProperties_comment_anyOf_i1) |
|                                                                                        |

<blockquote>

##### <a name="families_items_parents_items_anyOf_i1_additionalProperties_comment_anyOf_i0"></a>3.1.6.1. Property `item 0`

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
<blockquote>

##### <a name="families_items_parents_items_anyOf_i1_additionalProperties_comment_anyOf_i1"></a>3.1.6.2. Property `item 1`

| Type                      | `array of string`                                                         |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |
|                      |                    |

| Each item of this array must be                                                             | Description |
| ------------------------------------------------------------------------------------------- | ----------- |
| [items](#families_items_parents_items_anyOf_i1_additionalProperties_comment_anyOf_i1_items) | -           |
|                                                                                             |             |

##### <a name="families_items_parents_items_anyOf_i1_additionalProperties_comment_anyOf_i1_items"></a>3.1.6.2.1. items

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>

</blockquote>

</blockquote>
</details>

<details>
<summary><strong> <a name="families_items_parents_items_anyOf_i1_additionalProperties_notes"></a>3.1.7. [Optional] Property notes</strong>  

</summary>
<blockquote>

**Title:** Notes

| Type                      | `combining`                                                               |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

<blockquote>

| Any of(Option)                                                                       |
| ------------------------------------------------------------------------------------ |
| [item 0](#families_items_parents_items_anyOf_i1_additionalProperties_notes_anyOf_i0) |
| [item 1](#families_items_parents_items_anyOf_i1_additionalProperties_notes_anyOf_i1) |
|                                                                                      |

<blockquote>

##### <a name="families_items_parents_items_anyOf_i1_additionalProperties_notes_anyOf_i0"></a>3.1.7.1. Property `item 0`

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
<blockquote>

##### <a name="families_items_parents_items_anyOf_i1_additionalProperties_notes_anyOf_i1"></a>3.1.7.2. Property `item 1`

| Type                      | `array of string`                                                         |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |
|                      |                    |

| Each item of this array must be                                                           | Description |
| ----------------------------------------------------------------------------------------- | ----------- |
| [items](#families_items_parents_items_anyOf_i1_additionalProperties_notes_anyOf_i1_items) | -           |
|                                                                                           |             |

##### <a name="families_items_parents_items_anyOf_i1_additionalProperties_notes_anyOf_i1_items"></a>3.1.7.2.1. items

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>

</blockquote>

</blockquote>
</details>

<details>
<summary><strong> <a name="families_items_parents_items_anyOf_i1_additionalProperties_alias"></a>3.1.8. [Optional] Property alias</strong>  

</summary>
<blockquote>

**Title:** Alias

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
</details>

<details>
<summary><strong> <a name="families_items_parents_items_anyOf_i1_additionalProperties_from"></a>3.1.9. [Optional] Property from</strong>  

</summary>
<blockquote>

**Title:** From

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
</details>

<details>
<summary><strong> <a name="families_items_parents_items_anyOf_i1_additionalProperties_todo"></a>3.1.10. [Optional] Property todo</strong>  

</summary>
<blockquote>

**Title:** Todo

| Type                      | `combining`                                                               |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

<blockquote>

| Any of(Option)                                                                      |
| ----------------------------------------------------------------------------------- |
| [item 0](#families_items_parents_items_anyOf_i1_additionalProperties_todo_anyOf_i0) |
| [item 1](#families_items_parents_items_anyOf_i1_additionalProperties_todo_anyOf_i1) |
|                                                                                     |

<blockquote>

##### <a name="families_items_parents_items_anyOf_i1_additionalProperties_todo_anyOf_i0"></a>3.1.10.1. Property `item 0`

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
<blockquote>

##### <a name="families_items_parents_items_anyOf_i1_additionalProperties_todo_anyOf_i1"></a>3.1.10.2. Property `item 1`

| Type                      | `array of string`                                                         |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |
|                      |                    |

| Each item of this array must be                                                          | Description |
| ---------------------------------------------------------------------------------------- | ----------- |
| [items](#families_items_parents_items_anyOf_i1_additionalProperties_todo_anyOf_i1_items) | -           |
|                                                                                          |             |

##### <a name="families_items_parents_items_anyOf_i1_additionalProperties_todo_anyOf_i1_items"></a>3.1.10.2.1. items

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>

</blockquote>

</blockquote>
</details>

<details>
<summary><strong> <a name="families_items_parents_items_anyOf_i1_additionalProperties_pics"></a>3.1.11. [Optional] Property pics</strong>  

</summary>
<blockquote>

**Title:** Pics

| Type                      | `array of string`                                                         |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |
|                      |                    |

| Each item of this array must be                                                 | Description |
| ------------------------------------------------------------------------------- | ----------- |
| [items](#families_items_parents_items_anyOf_i1_additionalProperties_pics_items) | -           |
|                                                                                 |             |

##### <a name="families_items_parents_items_anyOf_i1_additionalProperties_pics_items"></a>3.1.11.1. items

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
</details>

<details>
<summary><strong> <a name="families_items_parents_items_anyOf_i1_additionalProperties_docs"></a>3.1.12. [Optional] Property docs</strong>  

</summary>
<blockquote>

**Title:** Docs

| Type                      | `array of string`                                                         |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |
|                      |                    |

| Each item of this array must be                                                 | Description |
| ------------------------------------------------------------------------------- | ----------- |
| [items](#families_items_parents_items_anyOf_i1_additionalProperties_docs_items) | -           |
|                                                                                 |             |

##### <a name="families_items_parents_items_anyOf_i1_additionalProperties_docs_items"></a>3.1.12.1. items

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
</details>

<details>
<summary><strong> <a name="families_items_parents_items_anyOf_i1_additionalProperties_links"></a>3.1.13. [Optional] Property links</strong>  

</summary>
<blockquote>

**Title:** Links

| Type                      | `array of string`                                                         |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |
|                      |                    |

| Each item of this array must be                                                  | Description |
| -------------------------------------------------------------------------------- | ----------- |
| [items](#families_items_parents_items_anyOf_i1_additionalProperties_links_items) | -           |
|                                                                                  |             |

##### <a name="families_items_parents_items_anyOf_i1_additionalProperties_links_items"></a>3.1.13.1. items

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
</details>

<details>
<summary><strong> <a name="families_items_parents_items_anyOf_i1_additionalProperties_gender"></a>3.1.14. [Optional] Property gender</strong>  

</summary>
<blockquote>

**Title:** Gender

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
</details>

<details>
<summary><strong> <a name="families_items_parents_items_anyOf_i1_additionalProperties_class"></a>3.1.15. [Optional] Property class</strong>  

</summary>
<blockquote>

**Title:** Class

| Type                      | `array of string`                                                         |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `[]`                                                                      |
|                           |                                                                           |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |
|                      |                    |

| Each item of this array must be                                                  | Description |
| -------------------------------------------------------------------------------- | ----------- |
| [items](#families_items_parents_items_anyOf_i1_additionalProperties_class_items) | -           |
|                                                                                  |             |

##### <a name="families_items_parents_items_anyOf_i1_additionalProperties_class_items"></a>3.1.15.1. items

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-12-29 at 17:52:25 +0100