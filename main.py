// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/// @title Simple utilization-based interest rate model (Aave-style but simplified)
/// @notice This is NOT production ready. It is a teaching/demo implementation.
contract InterestRateModel {
    /// @notice All rates are expressed in ray (1e27), per second.
    /// For example, 5% APR ~= 0.05 / 365 days ≈ 1.585e-9 per second.
    /// In ray: 1.585e-9 * 1e27 = 1.585e18.

    uint256 public immutable RAY = 1e27;

    /// @notice Base variable borrow rate when utilization is 0.
    uint256 public immutable baseVariableBorrowRate;

    /// @notice Slope of the borrow rate when utilization is below the kink.
