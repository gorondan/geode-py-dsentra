.. _pools:

Pool
==========

Initilizing 
--------------------------------------------------
.. py:method:: Geode.Portal.pool(poolID: int)

Initilize the Pool object of Geode with an existing pool id.

.. code-block:: python

    >> geode = Geode(exec_api, cons_key)
    ## You need pool id to create pool object
    >> poolID = 500191....78
    >> myPool = geode.Portal.pool(poolID)




Pool Ownership
----------------------

.. py:method:: NAME
  ..py:property::


``NAME`` is the name of the pool that given from creator of the pool.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> print("NAME:",myPool.NAME)
    NAME: Ice Pool

.. py:method:: CONTROLLER
  ..py:property::


``CONTROLLER`` ethereum address of the controller of the pool


.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    ##'0x2C95BC18Fd9382a07776D416EeF6c2FEb3AD2A8C'
    >> print("CONTROLLER:", myPool.CONTROLLER)
    CONTROLLER: '0x2C95BC18Fd9382a07776D416EeF6c2FEb3AD2A8C'


.. py:method:: initiated
  ..py:property::

``initiated`` (uint256) is timestamp of initiation time.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> print("initiated:",myPool.initiated)
    initiated: 1677379164


.. py:method:: maintainer
  ..py:property::

``maintainer`` (address) is the address of the maintainer.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> print("maintainer:",myPool.maintainer)
    
    maintainer: 0x2C95BC18Fd9382a07776D416EeF6c2FEb3AD2A8C


.. py:method:: yieldReceiver
  ..py:property::

``yieldReceiver`` (address) indicates the ethereum address of the reward collecter.

.. WARNING::
  If the ``yieldReceiver`` is not set or set to zero address ('0x00...0'), extra yields are shared among token holders.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> print("yieldReceiver:",myPool.yieldReceiver)
    
    yieldReceiver: '0xaa...a'


Pool Configuration
----------------------


.. py:method:: withdrawalCredential
  ..py:property::


``withdrawalCredential`` means that any reward generated by staking, can be obtained by ``withdrawalCredential``.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> print("withdrawalCredential:",myPool.withdrawalCredential)
    
    withdrawalCredential: 0x010000000000000000000000c82ed5ec571673e6b18c4b092c9cbc4ae86c786e


.. py:method:: withdrawalContract
  ..py:property::


Any reward of the pool earns will be sent to this ``withdrawalContract`` ethereum address. According to Ethereum standards, this address is also at the end of the withdrawal credentials.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> print("withdrawalContract:",myPool.withdrawalContract)
    
    withdrawalContract: 0xc82Ed5eC571673E6b18c4B092c9cbC4aE86C786e


.. py:method:: whitelist
  ..py:property::


Sometimes some maintainers may want to define a ``whitelist`` for the pool. In this case, you can see it with the whitelist command. If there is no white list, you will see 0x0000000000000000000000000000000000000000 address.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> print("whitelist:",myPool.whitelist)
    
    whitelist: 0x0000000000000000000000000000000000000000


.. py:method:: liquidityPool
  ..py:property::


    Address of the ``liquidityPool``.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> print("whitelist:",myPool.liquidityPool)
    
    liquidityPool: 0xEC5B756326f161bdc6506c16800ddF56765E0f3b


.. NOTE::

  Not all pools have whitelist or liquidityPool features.


.. py:method:: private
  ..py:property::


``private`` is the boolean value to either the pool is prived pool or public pool.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> print("private:",myPool.private)
    
    private: False


Pool Fee
----------------------

.. py:method:: fee
  ..py:property::



 Returns ``fee``(uint256) How much of the percentage from maintanence fee will received by the pool owner. DENOMINATOR: 1e10 (100%).

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> print("fee:",myPool.fee)
    
    fee: 500000000


.. NOTE::
    If the pool owner or maintainer wants to update its ``fee``, the operations continue from the value named ``priorFee`` for a certain period of time after the fee changes so that it does not manipulate the pool momentarily. This period is 3 days and must be kept in the variable named ``feeSwitch``. At the end of the ``feeSwitch`` period, the updated ``fee`` comes into play, so users have the freedom to leave the pool according to their own interests.


.. py:method:: priorFee
  ..py:property::

``priorFee`` replaces ``fee`` when ``feeSwitch`` has reached.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> print("whitelist:",myPool.priorFee)
    
    priorFee: 0


.. py:method:: feeSwitch
  ..py:property::

``feeSwitch`` is effective until 3 days.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> print("feeSwitch:",myPool.feeSwitch)
    
    feeSwitch: 0

Token Data
----------------------

.. py:method:: middlewaresList

``middlewaresList`` list of (address)es 

.. WARNING::
  To avoid malfunctions, utilizing our standard middlewares is expected by the pool owners.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> print("middlewaresList:",myPool.middlewaresList())
    
    middlewaresList: ['0xdaED82d9a6a0282D9084375eb1Dc8c09440e2aB3']

.. py:method:: middlewares(index:uint256)
  ..py:property::

``middlewares`` returns you the middleware corresponding to the given index. If the index is too large, it will throw an error.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> print("middlewares:",myPool.middlewares(0))
    
    middlewares: '0xdaED82d9a6a0282D9084375eb1Dc8c09440e2aB3'

.. py:method:: middlewaresLen
  ..py:property::
    

``middlewaresLen`` returns the number of middlewares. If you want to achieve multiple middlewares, it can be used to set the limits of the loop before executing the above code.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> print("middlewaresLen:",myPool.middlewaresLen)
    
    middlewaresLen: 1

Operator Marketplace
---------------------

.. py:method:: allowance(operatorId: int)

``allowance`` allowance's of the operators that given ID.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> myOperator = geode.Portal.operator(operatorID)
    >> print("allowance:",myPool.allowance(operator=myOperator.ID))


.. py:method:: validators(index:uint256)

``validators`` Returns the pubkey of the validator corresponding to the given index.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    ## In bytes
    >> print("Pubkey:",myPool.validators(0))
    
    Pubkey: b'\x93&\xf6\xc0\x7f\x8a\xbd\x08.\xf8+\x19\'\x9c\xbb\xa7ak\x03\x95\xfb\x94}P\xcd-_\xef0=\xd6\x13\xab\xe3\x10\x87\x07zg\xfa\xa4w\xc0c\x1c\xc7"\x8d'

    ## In hex string
    >> print("Pubkey:", myPool.validators(0).hex())

    Pubkey: '9326f6c07f8abd082ef82b19279cbba7616b0395fb947d50cd2d5fef303dd613abe31087077a67faa477c0631cc7228d'


.. py:method:: validatorsList
  ..py:property::

  Returns ``validatorsList`` (List(bytes32)) All validator pubkeys that registered to this pool.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> print("validatorsList:",myPool.validatorsList)
    
    validatorsList: [b'\x93&\xf6\xc0\x7f\x8a\xbd\x08.\xf8+\x19\'\x9c\xbb\xa7ak\x03\x95\xfb\x94}P\xcd-_\xef0=\xd6\x13\xab\xe3\x10\x87\x07zg\xfa\xa4w\xc0c\x1c\xc7"\x8d']

.. py:method:: validatorsLen
  ..py:property::

``validatorsLen`` (uint256) number of validators in the pool. Size of validatorsList array.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> print("validatorsLen:",myPool.validatorsLen)
    
    validatorsLen: 1


.. py:method:: activeValidators(operatorId: int)


``activeValidators`` Validator pubkeys that currently operating.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> myOperator = geode.Portal.operator(operatorID)
    >> print("activeValidators:",myPool.activeValidators(operator=myOperator.ID))
    
.. NOTE::
    More than one operator can work in a pool. And each operator will have their own validators. You can get this information with the operator's ID.

.. py:method:: proposedValidators(operatorId: int)

``proposedValidators`` Validator pubkeys that are proposed by the operator.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> myOperator = geode.Portal.operator(operatorID)
    >> print("proposedValidators:",myPool.proposedValidators(operator=myOperator.ID))
    

.. py:method:: alienValidators(operatorId: int)

``alienValidators`` Validator pubkeys that are malicious to system, detected by Telescope.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> myOperator = geode.Portal.operator(operatorID)
    >> print("alienValidators:",myPool.alienValidators(operator=myOperator.ID))
    


Staking Related Data
----------------------

.. py:method:: surplus
  ..py:property::


``surplus`` (uint256) amount that is waiting to be delegated (useful when proposing a validator). 

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> print("surplus:",myPool.surplus)
    
    surplus: 1000000000000000000


.. py:method:: secured
  ..py:property::


``secured`` (uint256) amount that is waiting to be sent to delegated validators.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> print("secured:",myPool.secured)
    
    secured: 1000000000000000000


Internal Wallet
-------------------

Every ID has its own internal wallet within Portal. 
It accrues fees, makes things safer and easier for Node Operators etc.

.. py:method:: wallet
  ..py:property::


``wallet`` (uint256) amount (in ``wei``) in the internal wallet of the pool

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> print("wallet:",myPool.wallet)
    
    wallet: 10000000000000


Fallback Operator
----------------------

.. WARNING::

    Fallback Operator mechnanism is for advanced users. Most of the applications, will not need these functionalities.

.. py:method:: fallbackOperator
  ..py:property::

``fallbackOperator`` (uint256) is the ID of selected Operator as ``fallback``.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> print("fallbackOperator:",myPool.fallbackOperator)
    
    fallbackOperator: 0

.. py:method:: fallbackThreshold
  ..py:property::

``fallbackThreshold`` (uint256) means when ``fallbackThreshold``% of allowances are filled, ``fallbackOperator`` will have unlimited allowance.  

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> print("fallbackThreshold:",myPool.fallbackThreshold)
    
    fallbackThreshold: 0


Staking Functions
----------------------

.. py:method:: prepareProposeStake(deposit_data_path: str)

* Signed Ether Amount: 1 ETH

This method prepares for a validator proposal. 
It reads deposit data from a file path, validates it, and returns the ``public keys`` and ``signature``s for the proposal stake.

.. py:method:: prepareStake(deposit_data_path: str)

* Signed Ether Amount: 31 ETH

This function prepares a beacon stake by taking the path to a deposit data file as input.
        The deposit data file is validated by checking that it contains the required amount of Ether
        for the Beacon chain, that it is meant for the specified network, and that it is associated
        with the withdrawal credentials of the current operator.

        Once the deposit data has been validated, the function extracts the public keys and
        signatures from the deposit data and returns them as a tuple.
