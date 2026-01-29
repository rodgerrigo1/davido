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
    uint256 public immutable slope1;

    /// @notice Slope of the borrow rate when utilization is above the kink.
    uint256 public immutable slope2;

    /// @notice Utilization point (in ray) where the slope changes.
    uint256 public immutable optimalUtilization;

    constructor(
        uint256 _baseVariableBorrowRate,
        uint256 _slope1,
        uint256 _slope2,
        uint256 _optimalUtilization
    ) {
        require(_optimalUtilization <= RAY, "INVALID_OPTIMAL_UTILIZATION");
        baseVariableBorrowRate = _baseVariableBorrowRate;
