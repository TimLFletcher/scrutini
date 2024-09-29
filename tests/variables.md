---
tags:
  - (Designer)
glightbox: false
---

# Variables

A variable lets you pass dynamic values into a component's properties, without you needing to manually edit a property each time the pipeline runs.

For example, you could define a variable "table_name", and set the [Create Table](/data-productivity-cloud/designer/docs/create-table/) component to use this variable for its **New Table Name** property. Each time you run the pipeline containing "table_name", you can set a new value for the variable, allowing you to re-use the same pipeline multiple times to create tables with different names, without editing the component's properties. Another advantage to variables would be if you have multiple components in a pipeline that all reference the same table. To reference a different table, you only need to change the value of the variable in one place, rather than edit the properties of each separate component.

Variables can also be accessed and set or re-set through Python scripts, giving you great flexibility in designing pipelines that are configured dynamically at runtime.

There are two classes of variable: **pipeline variables** and **project variables**. These are created, managed, and used in exactly the same way, and any mention of "variable" in this article should be understood to apply equally to both types, unless explicitly stated otherwise. Each type has a different **scope**, however, as defined in the following section on [Variable scope](#variable-scope).

**Grid variables** are a special type of pipeline variable. A grid variable is two-dimensional array that holds multiple values in named columns. This variable type is fully explained in [Grid variables](/data-productivity-cloud/designer/docs/grid-variables).

---

## Variable scope

The scope of a **project variable** is the entire project in which it is created. That is, any pipeline in any branch of the current project can use the same variable. A project variable can be given a different default value in different project environments.

The scope of a **pipeline variable** is the single pipeline in which it is created. No other pipeline in the project will be able to see the variable, though an identically named variable could be created in other pipelines.

A pipeline variable can be given the same name as a project variable. Where this happens, only the pipeline variable will be used within that specific pipeline, not the project variable. For avoidance of confusion, we recommend that you don't use the same names for different variables.

---

## Using variables

Variables can be used to provide property values in many components. The documentation for each component will tell you whether it supports the use of variables in properties.

To use a variable in a _string_ property, type the name of the variable surrounded by { } brackets and prefixed by the dollar symbol, as follows: `${variable}`.

For example, if you have defined a variable called "table_name", which will specify the name of a new table to be created by the Create Table component in your pipeline, you will enter `${table_name}` for the component's **New Table Name** property.

To use a variable in a property with a drop-down list of options, the drop-down will include all currently defined variables for you to choose from.

When a pipeline run begins, all of its variables are initialized with the default value that was specified when the variable was created. Variable values can be assigned or reassigned dynamically while the pipeline runs, typically through the use of [Python scripts](/data-productivity-cloud/designer/docs/python-script) or the [Update Scalar](/data-productivity-cloud/designer/docs/update-scalar) component. Values set in this way are valid only for the current run of the pipeline, and for the next run of the pipeline the variable will revert to its default value, or a new value must be assigned.

You can query the current value of a variable at any point in a pipeline by using a [Print Variables](/data-productivity-cloud/designer/docs/print-variables) component.

Variables can be used in file path parameters when addressing a storage bucket or data lake from a pipeline component. For details of this feature, read [Organizing file storage](/data-productivity-cloud/designer/docs/organizing-file-storage)

---

## Creating variables

1. Open a pipeline on the [pipeline canvas](/data-productivity-cloud/designer/docs/designer-ui-basics#the-pipeline-canvas). If you don't open a pipeline, you will still be able to create a project variable, but not a pipeline variable.
1. Click the **Variables** tab to see all pipeline and project variables available to the current pipeline. In this tab, you can edit or delete any existing variables, or create a new variable.
1. Click **Add** to open the **Add a variable** dialog.
1. Select either **Project variable** or **Pipeline variable**.
1. Complete the following fields, and then click **Create**:

   - **Variable name:** Each variable must have a unique name within its [scope](#variable-scope). For example, each pipeline variable must be uniquely named in this pipeline, though a variable with the same name can be defined in a different pipeline. A pipeline variable can have the same name as a project variable. Variable names can include letters, digits, and underscores, but can't begin with a digit. For example, `my_table_02` and `_02_my_table` are valid names, but `02_my_table` is not. A variable name must not be a JavaScript reserved word (e.g. `var` or `const`). If you want to use the variable in a Python or Bash script, it must not have the same name as a reserved word in those scripts.
   - **Description:** A description to inform other users of the purpose of the variable. This is optional, but its use is recommended.
   - **Type:** Select **Text**, **Number**, or **Grid**. See [Variable type](#variable-type), below, for an explanation of variable typing.
   - **Visibility:** Only used for pipeline variables. Select **Public** or **Private**. See [Variable visibility](#variable-visibility), below, for an explanation of variable visibility.
   - **Behavior:** Select **Shared** or **Copied**. See [Variable behavior](#variable-behavior-copied-or-shared), below, for an explanation of these options. The default behavior is **Shared**.
   - **Default value:** Only used for pipeline variables. The value initially assigned to a pipeline variable when a pipeline runs. The variable's value can be re-set by components as the pipeline runs, but it will always begin each new pipeline run with its default value.
   - **Environment default override:** Only used for project variables. The value initially assigned to a project variable when a pipeline runs. The variable's value can be re-set by components as the pipeline runs, but it will always begin each new pipeline run with its default value. This value can different for each different environment in the project.

---

## Variable type

The **Type** assigned to a variable determines what kind of information it contains. Variables can have one of the following types:

| Type   | Description                                                                                                                                                                                                                |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Text   | Any text string.                                                                                                                                                                                                           |
| Number | Any number, with or without decimals.                                                                                                                                                                                      |
| Grid   | A grid variable. Available for pipeline variables only. Grid variables differ considerably from other variables, and are documented separately in [Grid variables](/data-productivity-cloud/designer/docs/grid-variables). |

It is important that the variable type matches the data type of the property you want to use the variable in. For example, the **New Table Name** property is type _string_, so it requires a Text variable type. **Timeout** is type _integer_, so it requires a Numeric variable type.

Note that while the value of a Text variable might contain digits, for example `1234`, its type is still Text, and so it can't be used where a Numeric type is required.

---

## Variable visibility

Setting the correct visibility for a pipeline variable is important when you want to call a pipeline from another pipeline, using the [Run Orchestration](/data-productivity-cloud/designer/docs/run-orchestration) or [Run Transformation](/data-productivity-cloud/designer/docs/run-transformation) components.

A **Private** pipeline variable is only visible to the pipeline it is defined in. If the pipeline is called from another pipeline, the calling pipeline can't "see" the Private variable and so can't use its value, reset its value, or otherwise interact with it in any way.

A **Public** pipeline variable is visible outside the pipeline it is defined in, so it can be "seen" and used by any pipeline that calls the pipeline where it's set.

This only applies to pipeline variables. Project variables are automatically visible to every pipeline within the project.

--

## Variable behavior (copied or shared)

This refers to the "branching behavior" of a variable inside a pipeline. A "branch" in this context means a divergence of connectors within the pipeline, for example following the result from an [If](/data-productivity-cloud/designer/docs/if) component, giving the pipeline a branched structure with both (or all) branches of the pipeline running in parallel. This behavior applies to both pipeline variables and job variables.

Because a variable may be used in all branches of the pipeline, you need to specify how it will behave when updated within any one branch. There are two behavior options, **Copied** and **Shared**.

- **Copied** variables can be updated within one branch of the pipeline without updating the same variable in other branches. Effectively, each branch has its own copy of the variable, which is unaffected by changes to the copies used by any other branch. If the branches later rejoin, for example through the use of an [And](/data-productivity-cloud/designer/docs/and) or [Or](/data-productivity-cloud/designer/docs/or) component, the variable will revert to its _default_ value, regardless of any updates made in either branch.
- **Shared** variables are updated in a pipeline-wide fashion. If a shared variable value is updated in one branch, all other branches will use that updated value from that point in time onwards.

---

## Using variables in scripts

### Python scripts

Variables are visible to Python scripts created in the [Python Script](/data-productivity-cloud/designer/docs/python-script) component, and in those scripts they will act as any other Python variable. For example, to show the value of a pipeline variable `myVar` you can use the following Python command:

```
print (myVar)
```

From the Python script, you can use Python's `context` object to assign a new value to the variable. For example:

```
context.updateVariable ('myVar', 'a_new_value')
```

This new value for the variable will now be used in all subsequent components as the pipeline continues to run. This gives you a powerful tool for creating complex yet flexible pipelines, as some very simple Python scripts can dynamically change the behavior of the pipeline at runtime by manipulating variable values.

Note that you can manipulate the variable in any desired way within the Python script, but the value of the variable within the pipeline itself won't change unless you pass it back with the `context` object.

!!! warning

    Python will allow you to change the type of a variable, for example by assigning a string to a variable that previously held an integer. When you intend to pass the variable back to the pipeline using the `context` object, you must take care that you do **not** change the variable type in your Python script. Doing so will have consequences in your pipeline and will likely cause it to fail.

A full discussion of Python scripting is beyond the scope of this article. Refer to any good Python reference for further information.

### Bash scripts

Variables are visible to Bash scripts created in the [Bash Script](/data-productivity-cloud/designer/docs/bash-script) component. Variables are read-only in Bash scripts; their values can't be updated and passed back to the pipeline.

To use a variable in a Bash script, prefix the variable name with `$`, as follows:

```
echo $myVar
```

## Passing variables between pipelines

Variables can be used to pass values between pipelines when you call one pipeline from another using the [Run Orchestration](/data-productivity-cloud/designer/docs/run-orchestration) and [Run Transformation](/data-productivity-cloud/designer/docs/run-transformation) components.

You can reset the value of the variable when it's passed to the child by using the **Set Scalar Variables** property of the Run Orchestration/Transformation component. You can also dynamically reset the value through a component running in the child pipeline. When assigning a new value to a variable passed from parent to child, ensure that the new value is of the correct [type](#variable-type).
